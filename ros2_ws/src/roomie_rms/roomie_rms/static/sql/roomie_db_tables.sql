
-- roomie DB Table Definitions

CREATE TABLE floor (
    id INT PRIMARY KEY,
    name VARCHAR(8)
);

CREATE TABLE location_type (
    id INT PRIMARY KEY,
    name VARCHAR(16)
);

CREATE TABLE location (
    id INT PRIMARY KEY,
    name VARCHAR(16),
    location_type_id INT,
    is_destination BOOLEAN,
    floor_id INT,
    location_x FLOAT,
    location_y FLOAT,
    FOREIGN KEY (location_type_id) REFERENCES location_type(id),
    FOREIGN KEY (floor_id) REFERENCES floor(id)
);

CREATE TABLE task_type (
    id INT PRIMARY KEY,
    name VARCHAR(16)
);

CREATE TABLE task_status (
    id INT PRIMARY KEY,
    name VARCHAR(16)
);

CREATE TABLE robot_status (
    id INT PRIMARY KEY,
    name VARCHAR(16)
);

CREATE TABLE error (
    id INT PRIMARY KEY,
    name VARCHAR(16)
);

CREATE TABLE task (
    id INT PRIMARY KEY,
    type_id INT,
    task_status_id INT,
    location_id INT,
    robot_id INT,
    task_creation_time DATETIME,
    robot_assignment_time DATETIME,
    pickup_completion_time DATETIME,
    delivery_arrival_time DATETIME,
    task_completion_time DATETIME,
    task_cancellation_time DATETIME
);

CREATE TABLE robot (
    id INT PRIMARY KEY,
    name VARCHAR(16),
    model_name VARCHAR(16),
    installation_date DATE
);

CREATE TABLE robot_current_state (
    robot_id INT PRIMARY KEY,
    robot_status_id INT,
    location_id INT,
    battery_level FLOAT,
    error_id INT,
    last_updated_time DATETIME,
    FOREIGN KEY (robot_id) REFERENCES robot(id),
    FOREIGN KEY (robot_status_id) REFERENCES robot_status(id),
    FOREIGN KEY (location_id) REFERENCES location(id),
    FOREIGN KEY (error_id) REFERENCES error(id)
);

CREATE TABLE robot_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    robot_id INT,
    robot_status_id INT,
    task_id INT,
    location_id INT,
    error_id INT,
    record_time DATETIME,
    FOREIGN KEY (robot_id) REFERENCES robot(id),
    FOREIGN KEY (robot_status_id) REFERENCES robot_status(id),
    FOREIGN KEY (task_id) REFERENCES task(id),
    FOREIGN KEY (location_id) REFERENCES location(id),
    FOREIGN KEY (error_id) REFERENCES error(id)
);

CREATE TABLE `order` (
    id INT PRIMARY KEY,
    task_id INT,
    location_id INT,
    total_price INT,
    FOREIGN KEY (task_id) REFERENCES task(id),
    FOREIGN KEY (location_id) REFERENCES location(id)
);

CREATE TABLE food (
    id INT PRIMARY KEY,
    name VARCHAR(16),
    price INT,
    image VARCHAR(255)
);

CREATE TABLE food_order_item (
    id INT PRIMARY KEY,
    order_id INT,
    food_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES `order`(id),
    FOREIGN KEY (food_id) REFERENCES food(id)
);

CREATE TABLE supply (
    id INT PRIMARY KEY,
    name VARCHAR(16),
    image VARCHAR(255)
);

CREATE TABLE supply_order_item (
    id INT PRIMARY KEY,
    order_id INT,
    supply_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES `order`(id),
    FOREIGN KEY (supply_id) REFERENCES supply(id)
);
