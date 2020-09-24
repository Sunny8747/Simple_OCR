# Simple_OCR

## 배포중인 무료 프로그램을 위한 Simple OCR

-   현 상태의 배포중인 프로그램에서는 특정 목록을 배정하기 위하여 직접 참석 인원 구분을 한다.
-   전체 인원 목록은 불러올 수 있지만 참석 유무는 직접 눈으로 시스템을 보고 확인하는 수 밖에 없음.
-   따라서 OCR을 통하여 해당 화면을 인식하여 참석유무를 판별해주는 시스템을 추가하려고 함.
-   오픈소스 ocr인 teseract나 easyOCR등은 용량이 크거나 사용자에게 추가적인 프로그램 설치를 강요하기때문에 직접 개발하기로 결정
-   tensorflow기반 간단한 화면 캡쳐사진을 ocr 하는것으로 목표

## image modification and labeling

-   image modification을 통하여 ocr이 필요한 image 정제 필요.
