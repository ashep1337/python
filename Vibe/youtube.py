from datetime import datetime, timedelta, timezone

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes needed: read-only access to YouTube account
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=creds)


def get_subscriptions(youtube):
    subscriptions = []
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)
    while request:
        response = request.execute()
        for item in response.get("items", []):
            channel_id = item["snippet"]["resourceId"]["channelId"]
            subscriptions.append(channel_id)
        request = youtube.subscriptions().list_next(request, response)
    return subscriptions


def get_recent_videos(youtube, channel_id, hours=24):
    # Get the channel’s uploads playlist
    response = youtube.channels().list(part="contentDetails", id=channel_id).execute()

    if "items" not in response or not response["items"]:
        # No data for this channel
        return []

    content_details = response["items"][0].get("contentDetails", {})
    uploads_playlist_id = content_details.get("relatedPlaylists", {}).get("uploads")

    if not uploads_playlist_id:
        # Channel has no uploads playlist
        return []

    # Get recent videos (up to 10 per channel to check for new ones)
    try:
        request = youtube.playlistItems().list(
            part="snippet", playlistId=uploads_playlist_id, maxResults=10
        )
        response = request.execute()
    except Exception as e:
        print(f"Skipping channel {channel_id} due to error: {e}")
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)

    videos = []
    for item in response.get("items", []):
        published_at = datetime.fromisoformat(
            item["snippet"]["publishedAt"].replace("Z", "+00:00")
        )
        if published_at > cutoff:
            videos.append(
                {
                    "title": item["snippet"]["title"],
                    "videoId": item["snippet"]["resourceId"]["videoId"],
                    "publishedAt": published_at,
                }
            )
    return videos


if __name__ == "__main__":
    youtube = get_authenticated_service()

    subscriptions = get_subscriptions(youtube)
    print(f"Found {len(subscriptions)} subscriptions.")

    for channel_id in subscriptions:
        videos = get_recent_videos(youtube, channel_id, hours=24)
        if videos:
            print(f"\nChannel {channel_id} uploaded in the last 24h:")
            for v in videos:
                print(
                    f"- {v['title']} ({v['publishedAt']}) https://youtu.be/{
                        v['videoId']
                    }"
                )
