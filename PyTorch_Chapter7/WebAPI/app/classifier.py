# classifier.py
from torch import nn
from torchvision import transforms, models
def create_network():
    # resnet18 읽기
    # 파라미터는 뒤에서 설정하므로 pretrained=True는 필요 없다
    net = models.resnet18()
    
   # 마지막 계층을 2출력의 선형 계층으로 변경
    fc_input_dim = net.fc.in_features
    net.fc = nn.Linear(fc_input_dim, 2)
    return net

class Classifier(object):
    def __init__(self, params):
        # 식별 네트워크 작성
        self.net = create__network()
        # 학습 완료 파라미터 설정
        self.net.load_state_dict(params)
        # 평가 모드로 설정
        self.net.eval()
        # 이미지를 Tensor로 변환하는 함수
        self.transformer = transforms.Compose([
            transforms.CenterCrop(224),
            transforms.ToTensor()
        ])
        # 분류ID와 분류명 연결
        self.classes = ["burrito", "taco"]
    def predict(self, img):
        # 이미지를 Tensor로 변환
        x = self.transformer(img)
        # PyTorch는 항상 배치로 처리하므로
        # batch의 차원을 선두에 추가
        x = x.unsqueeze(0)
        # 신경망의 출력 계산
        out = self.net(x)
        out = out.max(1)[1].item()
        # 예측한 분류명 반환
        return self.classes[out]
