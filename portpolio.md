# 🇧🇷 브라질 이커머스 초기 시장 진입 전략 분석 (Brazil E-Commerce Market Entry Strategy)

![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=flat-square&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

> **"무엇을 팔 것인가보다, 어디서 시작할 것인가?"** > 10만 건의 Olist 거래 데이터를 기반으로 지역별 물류 편차 리스크를 최소화하고, 초기 시장 안착 성공률을 극대화할 수 있는 **최적 진입점(Entry Point)**을 도출한 데이터 분석 프로젝트입니다.

---

## 📌 1. 프로젝트 개요 (Overview)
[cite_start]브라질은 거대한 영토로 인해 지역별 소비 성향과 물류 인프라의 격차가 매우 큰 시장입니다. [cite: 48, 55] 본 프로젝트는 브라질 이커머스 기업 Olist의 실제 데이터를 활용하여, **단기 매출보다는 초기 시장 안착(인지도 확보 및 고객 만족)**을 목표로 하는 최적의 진입 지역과 카테고리를 선정하는 것을 목표로 합니다.

* **기간:** 2026.XX.XX ~ 2026.XX.XX (약 X주)
* [cite_start]**데이터셋:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce) (100k orders) [cite: 11]
* **역할:** 데이터 전처리, 가중치 기반 스코어링 모델 설계, 경쟁자 분석, 전략 수립

<br/>

## ❓ 2. 문제 정의 (Problem Definition)
### ⚠️ 배경 및 제약 사항
1.  [cite_start]**높은 물류 리스크:** 브라질은 물류비용과 배송 기간의 지역 편차가 극심하여, 전 지역 동시 진출 시 운영 리스크가 큼 [cite: 48, 49]
2.  [cite_start]**선택과 집중의 필요성:** 초기 자원이 한정된 상황에서 "어느 지역의 어떤 카테고리"를 공략해야 실패 확률을 낮출 수 있는지가 핵심 의사결정 사항임 [cite: 50, 55]

### 🎯 목표
* 단순 매출 상위 지역이 아닌, **물류 효율성**과 **고객 만족도**를 동시에 확보할 수 있는 거점 발굴
* 경쟁 강도 대비 수요가 충분한 **기회 시장(Underserved Market)** 식별

<br/>

## 🏗️ 3. 분석 아키텍처 및 방법론 (Architecture & Methodology)

### 3-1. 전체 데이터 파이프라인
![Architecture Diagram](https://placehold.co/800x200?text=Raw+Data+->+Preprocessing+->+Feature+Engineering+->+Scoring+->+Validation)
*(여기에 아키텍처 다이어그램 이미지를 첨부하면 좋습니다)*

1.  **Preprocessing:** 9개 관계형 테이블 병합(Merge) 및 결측치/이상치 처리
2.  **Feature Engineering:**
    * `Opportunity Score` = 수요(Demand) × 불만족도(Dissatisfaction)
    * `Delay Conversion Rate`: 배송 지연이 낮은 평점으로 전환되는 비율
3.  **Weighted Scoring:** 비즈니스 목표(초기 안착)에 맞춰 지표별 가중치 차등 부여
4.  **Cross Validation:** 경쟁자 데이터(Seller Count)를 활용한 시장 진입 타당성 검증

### 3-2. 의사결정 프레임워크 (Decision Framework)
[cite_start]지역(Location)과 상품(Category)을 독립 변수로 평가한 후 결합하는 이원화 전략을 사용했습니다. [cite: 63, 87]

| 구분 | 평가 지표 (Metrics) | 가중치 의도 (Rationale) |
|:---:|:---|:---|
| **지역** | 1. 수요 대비 배송 불만족도 (기회 점수)<br>2. 배송비 비율<br>3. 배송 지연 시 평점 하락률 | [cite_start]수요가 많지만 서비스가 열악해 **개선 여지(기회)**가 큰 지역을 우선순위로 둠 [cite: 88] |
| **상품** | 1. 배송비 대비 평점 (품질)<br>2. 재구매 가능성<br>3. 총 판매량 및 매출 | [cite_start]단기 매출보다는 **품질 인식**과 **재구매**를 통해 안정적 기반을 다질 수 있는 상품군 선정 [cite: 90] |

<br/>

## 📊 4. 데이터 분석 결과 (Key Findings)

### 📍 Insight 1. 기회 점수(Opportunity Score) 기반 지역 선정
* 단순 주문량(Order Count)은 SP(상파울루)가 압도적이지만, 경쟁이 치열하고 배송 만족도가 이미 높음.
* [cite_start]분석 결과, **RJ(리우데자네이루)** 지역이 높은 수요 밀도를 가지면서도 물류 효율 개선 시 고객 만족도를 크게 높일 수 있는 **최적의 기회 지역**으로 식별됨. [cite: 366]

### 🛍️ Insight 2. 안정적 수익원(Cash Cow) 카테고리 발굴
* **Health_Beauty (건강/미용)** 카테고리가 높은 재구매율과 배송비 저항성이 낮은 특성을 보임.
* [cite_start]필수 소비재 성격이 강해 초기 브랜드 인지도 확보에 유리함. [cite: 369]

### 🛡️ Insight 3. 경쟁자 분석을 통한 타당성 검증
* `Orders per Seller` (셀러 1인당 주문 수) 지표 분석 결과, **RJ × Health_Beauty** 조합은 수요 대비 공급자 수가 상대적으로 부족한 **공급 공백(Underserved)** 시장임이 확인됨.
* [cite_start]따라서 진입 시 배송 경쟁력을 무기로 시장 점유율을 빠르게 확보할 수 있음. [cite: 478]

<br/>

## 🚀 5. 결론 및 전략 (Conclusion & Strategy)

> **최종 전략: "RJ(리우데자네이루) 지역에서 Health & Beauty 카테고리로 런칭"**

1.  **진입 거점:** **RJ (Rio de Janeiro)**
    * 이유: 높은 수요 밀도 + 물류 효율화 시 이익 극대화 가능
2.  **핵심 상품:** **Health_Beauty**
    * 이유: 안정적인 재구매 수요 + 낮은 물류 민감도
3.  **기대 효과:**
    * 고비용/고위험의 전 지역 확산 전략 대비 초기 운영 비용 절감
    * 데이터 기반의 타겟팅을 통해 마케팅 ROI 최적화 및 안정적 리뷰 데이터 확보

<br/>

## 📂 6. 폴더 구조 (Repository Structure)
```bash
├── data/                  # Raw and Processed Data (Not included in repo)
├── notebooks/             # Jupyter Notebooks for Analysis
│   ├── 01_Data_Preprocessing.ipynb
│   ├── 02_EDA_Category_Analysis.ipynb
│   ├── 03_EDA_Location_Analysis.ipynb
│   └── 04_Scoring_and_Strategy.ipynb
├── src/                   # Source code for utility functions
├── images/                # Images for README and Reports
└── README.md              # Project Overview
