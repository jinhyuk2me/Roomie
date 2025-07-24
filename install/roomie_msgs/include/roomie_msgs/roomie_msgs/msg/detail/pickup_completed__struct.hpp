// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roomie_msgs:msg/PickupCompleted.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/pickup_completed.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_HPP_

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
# define DEPRECATED__roomie_msgs__msg__PickupCompleted __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__msg__PickupCompleted __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PickupCompleted_
{
  using Type = PickupCompleted_<ContainerAllocator>;

  explicit PickupCompleted_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
    }
  }

  explicit PickupCompleted_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _task_id_type =
    int32_t;
  _task_id_type task_id;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
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

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::msg::PickupCompleted_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::msg::PickupCompleted_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::PickupCompleted_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::PickupCompleted_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__msg__PickupCompleted
    std::shared_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__msg__PickupCompleted
    std::shared_ptr<roomie_msgs::msg::PickupCompleted_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PickupCompleted_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->task_id != other.task_id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const PickupCompleted_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PickupCompleted_

// alias to use template instance with default allocator
using PickupCompleted =
  roomie_msgs::msg::PickupCompleted_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_HPP_
