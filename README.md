# 2DGP
2DGP

#1. 게임의 소개

- 제목:The Binding of issac
-그래픽은 2D 카툰식 그래픽이며 다양한 아이템들로 자신의 눈물 강화하거나 신체를 강화하고 눈물을 발사하여 적들을 맞춰 여러 보스들을 물리치는 게임이다.
- 게임의 목적, 방법 등 간단한 설명
-wasd로 움직이며 방향키로 눈물 발사, e키로 폭탄을 놓을 수 있으며 스페이스바로 아이템을 사용할 수 있다 .칼을 들고 주인공인 아이작을 죽이려는 어머니르 피해 지하로 도망쳐 
자신의 눈물로 물리치고 마지막엔 본인과의 싸움도 하는 게임이다. 체력이 다 깎이면 게임오버 되는 방식으로 세이브나 로드가 없어 한번 시작하면 끝을 봐야하는 게임이다.

#2. GameState (Scene) 의 수 및 각각의 이름
 첫 스테이지에 약 7~8개의 방이 있으며 황금방. 보스방, 상점이 있고 가시방.희생방,피묻은방,다이스방,책방 중에 랜덤으로 한두개가 나온다 보스를 깰때마다 스테이지가 바뀌며 방의 개수도 늘어난다. 여러 조건을 충족하면 10개의 스테이지를 갈 수 있으며 조건을 충족하지못하면 7스테이지에서 끝난다.

#3. 각 GameState 별 다음 항목
- 한줄짜리 설명
보스방, 황금방, 상점 , 기본 방들이 있는 맵
- 화면에 표시할 객체들의 목록
보스방, 황금방, 상점 ,기본방
- 처리할 키/마우스 등 이벤트
wasd(움직임) e(폭탄) 방향키(눈물 발사) 스페이스바 (아이템 사용)
- 다른 State 로 이동한다면, 각 이동에 대한 조건 및법
방에있는 몬스터들을 다 처치하면 문이 열린다.


#4. 필요한 기술
- 다른 과목에서 배운 기술  :
여러 언어 관련된 지식
- 이 과목에서 배울 것으로 기대되는 :
캐릭터 생성 , 움직임, 아이템 적용, BGM 넣기. 
![20200925_134658](https://user-images.githubusercontent.com/70678897/94227527-abdda280-ff35-11ea-9975-2be0f5d46b79.png)
![20200925_134722](https://user-images.githubusercontent.com/70678897/94227533-aed89300-ff35-11ea-8895-f8d4364c3ead.png)
![슬라이드5](https://user-images.githubusercontent.com/70678897/95649159-10445880-0b17-11eb-8f06-4570ced00b46.JPG)
![슬라이드6](https://user-images.githubusercontent.com/70678897/95649160-11758580-0b17-11eb-9871-db03f1ad8baf.JPG)
![슬라이드3](https://user-images.githubusercontent.com/70678897/95649161-11758580-0b17-11eb-82c7-223b7897b0a5.JPG)
![슬라이드4](https://user-images.githubusercontent.com/70678897/95649163-120e1c00-0b17-11eb-85b1-a4c771ec687d.JPG)


