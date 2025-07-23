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
(0, 'LOB_WAITING', 0, FALSE, 0, NULL, NULL),
(1, 'LOB_CALL', 0, TRUE, 0, NULL, NULL),
(2, 'RES_PICKUP', 1, FALSE, 0, NULL, NULL),
(3, 'RES_CALL', 1, TRUE, 0, NULL, NULL),
(4, 'SUP_PICKUP', 1, FALSE, 0, NULL, NULL),
(5, 'ELE_F1', 3, FALSE, 0, NULL, NULL),
(6, 'ELE_F2', 3, FALSE, 1, NULL, NULL),
(7, 'ELE_F3', 3, FALSE, 2, NULL, NULL),
(8, 'ELE_F4', 3, FALSE, 3, NULL, NULL),
(101, 'ROOM_101', 2, TRUE, 0, NULL, NULL),
(102, 'ROOM_102', 2, TRUE, 0, NULL, NULL),
(201, 'ROOM_201', 2, TRUE, 1, NULL, NULL),
(202, 'ROOM_202', 2, TRUE, 1, NULL, NULL),
(301, 'ROOM_301', 2, TRUE, 2, NULL, NULL),
(302, 'ROOM_302', 2, TRUE, 2, NULL, NULL);

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
(0, '스파게티', 15000, ''),
(1, '피자', 31000, ''),
(2, '스테이크', 48000, ''),
(3, '버거', 11000, '');

-- supply: 비품 목록
INSERT INTO `supply` (id, name, image) VALUES
(0, '칫솔', ''),
(1, '타월', ''),
(2, '생수', ''),
(3, '수저', '');

-- robot: 로봇 정보
-- FK인 task_id는 task 테이블 생성 후 UPDATE
INSERT INTO `robot` (id, name, model_name, robot_status_id, task_id, floor_id, battery_status, error_id) VALUES
(0, 'ROBOT_01', 'ServeBot_V1', 2, NULL, 1, 85, NULL),
(1, 'ROBOT_02', 'ServeBot_V2', 3, NULL, 0, 45, NULL),
(2, 'ROBOT_03', 'ServeBot_V2', 2, NULL, 0, 95, NULL),
(3, 'ROBOT_04', 'ServeBot_V1', 1, NULL, 0, 75, NULL);

-- task: 작업 정보
INSERT INTO `task` (id, type_id, task_status_id, location_id, robot_id, task_creation_time, robot_assignment_time, pickup_completion_time, delivery_arrival_time, task_completion_time, task_cancellation_time) VALUES
(1, 0, 7, 201, 0, '2025-07-22 10:30:00', '2025-07-22 10:32:00', '2025-07-22 10:45:00', '2025-07-22 10:50:00', '2025-07-22 10:52:10', NULL),
(2, 1, 5, 302, 1, '2025-07-23 11:00:00', '2025-07-23 11:01:00', '2025-07-23 11:05:00', NULL, NULL, NULL),
(3, 2, 2, 101, 0, '2025-07-23 14:00:00', '2025-07-23 14:01:00', NULL, NULL, NULL, NULL),
(4, 0, 2, 202, 2, '2025-07-24 09:30:00', '2025-07-24 09:31:00', NULL, NULL, NULL, NULL),
(5, 1, 0, 102, NULL, '2025-07-24 18:00:00', NULL, NULL, NULL, NULL, NULL);

-- `order`: 주문 정보
INSERT INTO `order` (id, task_id, location_id, total_price) VALUES
(1, 1, 201, 15000),
(2, 2, 302, 0),
(3, 4, 202, 61000),
(4, 5, 102, 0);

-- food_order_item: 주문된 음식 항목
INSERT INTO `food_order_item` (id, order_id, food_id, quantity) VALUES
(1, 1, 0, 1),
(2, 3, 0, 2),
(3, 3, 1, 1);

-- supply_order_item: 주문된 비품 항목
INSERT INTO `supply_order_item` (id, order_id, supply_id, quantity) VALUES
(1, 2, 1, 3),
(2, 2, 2, 2),
(3, 4, 0, 2);

-- 로봇의 현재 작업 ID 업데이트
UPDATE `robot` SET task_id = 3 WHERE id = 0;
UPDATE `robot` SET task_id = 2 WHERE id = 1;
UPDATE `robot` SET task_id = 4 WHERE id = 2;
