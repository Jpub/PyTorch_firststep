# wsgi.py
import torch
from smart_getenv import getenv

from app import create_app
from app.classifier import Classifier

# 파라미터 파일의 경로를 환경 변수에서 읽기
prm_file = getenv("PRM_FILE", default="/data/taco_burrito.prm")
# 파라미터 파일 읽기
params = torch.load(prm_file,
                    map_location=lambda storage, loc: storage)
# Classifier와 Flask 애플리케이션 생성
classifier = Classifier(params)
app = create_app(classifier)
