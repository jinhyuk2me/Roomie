// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roomie_msgs:msg/RobotGuiEvent.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/robot_gui_event.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__msg__RobotGuiEvent __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__msg__RobotGuiEvent __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotGuiEvent_
{
  using Type = RobotGuiEvent_<ContainerAllocator>;

  explicit RobotGuiEvent_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->rgui_event_id = 0l;
      this->task_id = 0l;
      this->detail = "";
    }
  }

  explicit RobotGuiEvent_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_alloc, _init),
    detail(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->rgui_event_id = 0l;
      this->task_id = 0l;
      this->detail = "";
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _rgui_event_id_type =
    int32_t;
  _rgui_event_id_type rgui_event_id;
  using _task_id_type =
    int32_t;
  _task_id_type task_id;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;
  using _detail_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _detail_type detail;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__rgui_event_id(
    const int32_t & _arg)
  {
    this->rgui_event_id = _arg;
    return *this;
  }
  Type & set__task_id(
    const int32_t & _arg)
  {
    this->task_id = _arg;
    return *this;
  }
  Type & set__timestamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__detail(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->detail = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__msg__RobotGuiEvent
    std::shared_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__msg__RobotGuiEvent
    std::shared_ptr<roomie_msgs::msg::RobotGuiEvent_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotGuiEvent_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->rgui_event_id != other.rgui_event_id) {
      return false;
    }
    if (this->task_id != other.task_id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->detail != other.detail) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotGuiEvent_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotGuiEvent_

// alias to use template instance with default allocator
using RobotGuiEvent =
  roomie_msgs::msg::RobotGuiEvent_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_HPP_
