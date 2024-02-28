from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask("VideoAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, type=str, help='Title of the video')
parser.add_argument('duration', required=False, type=str, help='Duration of the video')
parser.add_argument('views', required=False, type=int, help='Views of the video')   
parser.add_argument('likes', required=False, type=int, help='Likes of the video')


videos = {
    'video1': {
        'title': 'Introduction to Python Programming',
        'duration': '1:30:00',
        'views': 1000,
        'likes': 50
    },
    'video2': {
        'title': 'Data Structures in Python',
        'duration': '2:00:00',
        'views': 800,
        'likes': 40
    },
    'video3': {
        'title': 'Web Development with Flask',
        'duration': '1:45:00',
        'views': 1200,
        'likes': 60
    },
    'video4': {
        'title': 'Machine Learning Basics',
        'duration': '2:30:00',
        'views': 1500,
        'likes': 70
    }
}


class Video(Resource):
    def get(self, video_id=None):
        if video_id is None or video_id == "all":
            return videos
        return videos.get(video_id, "Video not found")

    def put(self, video_id):
        args = parser.parse_args()
        new_video = {'title': args['title'], 'duration': args['duration'], 'views': args['views'], 'likes': args['likes']}
        videos[video_id] = new_video
        return {video_id: videos[video_id]}

    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f"Video {video_id} does not exist")
        del videos[video_id]
        return "", 204

class VideoSchedule(Resource):

    def get(self):
        return videos
    
    def post(self):
        args = parser.parge_args()
        new_video = {'title': args['title'], 'duration': args['duration'], 'views': args['views'], 'likes': args['likes']}
        video_id = max(int(v.lstrip('video')) for v in videos.keys()) + 1
        videos[video_id] = new_video
        return {video_id: videos[video_id]}

api.add_resource(Video, '/videos/<video_id>')
api.add_resource(VideoSchedule, '/videos/')

if __name__ == '__main__':
    app.run(debug=True)