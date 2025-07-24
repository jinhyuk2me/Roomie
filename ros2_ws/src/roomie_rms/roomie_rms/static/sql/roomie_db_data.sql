-- -----------------------------------------------------
-- 초기 데이터 INSERT
-- -----------------------------------------------------

-- floor: 층 정보
INSERT INTO `floor` (id, name) VALUES
(0, '1층'),
(1, '2층'),
(2, '3층'),
(3, '4층');

-- location_type: 장소 유형
INSERT INTO `location_type` (id, name) VALUES
(0, '로비'),
(1, '편의시설'),
(2, '객실'),
(3, '엘레베이터');

-- location: 상세 위치 정보
INSERT INTO `location` (id, name, location_type_id, is_destination, floor_id, location_x, location_y) VALUES
(0, 'LOB_WAITING', 0, FALSE, 0, -0.2, 0.5),
(1, 'LOB_CALL', 0, TRUE, 0, NULL, NULL),
(2, 'RES_PICKUP', 1, FALSE, 0, -0.3, 2.5),
(3, 'RES_CALL', 1, TRUE, 0, NULL, NULL),
(4, 'SUP_PICKUP', 1, FALSE, 0, -0.3, 4.5),
(5, 'ELE_1', 3, FALSE, 0, 9.25, 1.7),
(6, 'ELE_2', 3, FALSE, 1, NULL, NULL),
(101, 'ROOM_101', 2, TRUE, 0, 5.3, 3.5),
(102, 'ROOM_102', 2, TRUE, 0, 7.4, 3.5),
(201, 'ROOM_201', 2, TRUE, 1, NULL, NULL),
(202, 'ROOM_202', 2, TRUE, 1, NULL, NULL);

-- task_type: 작업 유형
INSERT INTO `task_type` (id, name) VALUES
(0, '음식배송'),
(1, '비품배송'),
(2, '호출'),
(3, '길안내');

-- task_status: 작업 상태
INSERT INTO `task_status` (id, name) VALUES
(0, '접수됨'),
(1, '준비 완료'),
(2, '로봇 할당됨'),
(3, '픽업 장소로 이동'),
(4, '픽업 대기 중'),
(5, '배송 중'),
(6, '배송 도착'),
(7, '수령 완료'),
(10, '호출 접수됨'),
(11, '호출 로봇 할당됨'),
(12, '호출 이동 중'),
(13, '호출 도착'),
(20, '길안내 접수됨'),
(21, '길안내 중'),
(22, '길안내 도착');

-- robot_status: 로봇 상태
INSERT INTO `robot_status` (id, name) VALUES
(0, '작업 불가능'),
(1, '작업 가능'),
(2, '작업 입력 중'),
(3, '작업 수행 중'),
(4, '복귀 대기 중'),
(5, '복귀 중'),
(6, '작업 실패'),
(7, '시스템 오류');

-- error: 에러 유형
INSERT INTO `error` (id, name) VALUES
(101, '작업실패'),
(102, '통신오류'),
(103, '시스템 오류');

-- food: 음식 메뉴
INSERT INTO `food` (id, name, price, image) VALUES
(0, '스파게티', 15000, '/images/food/spaghetti.jpg'),
(1, '피자', 31000, '/images/food/pizza.jpg'),
(2, '스테이크', 48000, '/images/food/steak.jpg'),
(3, '버거', 11000, '/images/food/burger.jpg');

-- supply: 비품 목록
INSERT INTO `supply` (id, name, image) VALUES
(0, '칫솔', '/images/supply/toothbrush.jpg'),
(1, '타월', '/images/supply/towel.jpg'),
(2, '생수', '/images/supply/water.jpg'),
(3, '수저', '/images/supply/spoon.jpg');

-- robot: 로봇 기본 정보 (정적 데이터)
INSERT INTO `robot` (id, name, model_name, installation_date) VALUES
(0, 'ROBOT_01', 'ServeBot_V1', '2024-03-04'),
(1, 'ROBOT_02', 'ServeBot_V2', '2025-06-17'),
(2, 'ROBOT_03', 'ServeBot_V2', '2025-06-17');
