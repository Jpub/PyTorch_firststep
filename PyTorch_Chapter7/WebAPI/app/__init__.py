# __init__.py
from flask import Flask, request, jsonify
from PIL import Image

def create_app(classifier):
    # Flask 애플리케이션 생성
    app = Flask(__name__)
    # POST / 요청을 처리하는 함수 정의
    @app.route("/", methods=["POST"])
    def predict():
        # 받은 파일의 핸들러 취득
        img_file = request.files["img"]
        
        # 파일이 비어있는지 확인
        if img_file.filename == "":
            return "Bad Request", 400
   
        # PIL을 사용해서 이미지 파일 읽기
        img = Image.open(img_file)
        
        # 식별 모델을 사용해서 타코스인지 부리토인지 예측
        result = classifier.predict(img)
        
        # 결과를 JSON 형식으로 반환
        return jsonify({
            "result": result
        })
    return app
