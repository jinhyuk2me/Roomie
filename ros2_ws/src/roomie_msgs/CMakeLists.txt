cmake_minimum_required(VERSION 3.8)
project(roomie_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

# Generate interfaces
rosidl_generate_interfaces(${PROJECT_NAME}
  # Messages - Robot Status
  "msg/robot_status/RobotState.msg"
  "msg/robot_status/BatteryStatus.msg"
  "msg/robot_status/RoomiePose.msg"
  "msg/robot_status/Arrival.msg"
  
  # Messages - Task Management
  "msg/task_management/TaskState.msg"
  "msg/task_management/PickupCompleted.msg"
  "msg/task_management/DeliveryCompleted.msg"
  
  # Messages - User Interface
  "msg/user_interface/RobotGuiEvent.msg"
  "msg/user_interface/TrackingEvent.msg"
  "msg/user_interface/Registered.msg"
  
  # Services - Robot Control
  "srv/robot_control/CreateTask.srv"
  "srv/robot_control/SetVSMode.srv"
  "srv/robot_control/Location.srv"
  "srv/robot_control/GetLocations.srv"
  
  # Services - Door/Elevator
  "srv/door_elevator/UnlockDoor.srv"
  "srv/door_elevator/ElevatorWidth.srv"
  "srv/door_elevator/ElevatorStatus.srv"
  "srv/door_elevator/DoorStatus.srv"
  
  # Services - Sensor
  "srv/sensor/ButtonStatus.srv"
  "srv/sensor/SpaceAvailability.srv"
  "srv/sensor/ReadCardInfo.srv"
  "srv/sensor/CheckItemLoaded.srv"
  "srv/sensor/CheckDoorState.srv"
  
  # Services - Task Management
  "srv/task_management/StartCountdown.srv"
  "srv/task_management/ReturnCountdown.srv"
  
  # Services - Security
  "srv/security/ControlLock.srv"
  
  # Actions
  "action/PerformTask.action"
  "action/PerformReturn.action"
  
  DEPENDENCIES
    geometry_msgs
    builtin_interfaces
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package() 