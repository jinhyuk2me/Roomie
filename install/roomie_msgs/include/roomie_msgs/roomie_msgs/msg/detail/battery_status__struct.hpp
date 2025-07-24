// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roomie_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/battery_status.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__roomie_msgs__msg__BatteryStatus __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__msg__BatteryStatus __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BatteryStatus_
{
  using Type = BatteryStatus_<ContainerAllocator>;

  explicit BatteryStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->charge_percentage = 0.0f;
      this->is_charging = false;
    }
  }

  explicit BatteryStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->charge_percentage = 0.0f;
      this->is_charging = false;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _charge_percentage_type =
    float;
  _charge_percentage_type charge_percentage;
  using _is_charging_type =
    bool;
  _is_charging_type is_charging;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__charge_percentage(
    const float & _arg)
  {
    this->charge_percentage = _arg;
    return *this;
  }
  Type & set__is_charging(
    const bool & _arg)
  {
    this->is_charging = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::msg::BatteryStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::msg::BatteryStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::BatteryStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::BatteryStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__msg__BatteryStatus
    std::shared_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__msg__BatteryStatus
    std::shared_ptr<roomie_msgs::msg::BatteryStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BatteryStatus_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->charge_percentage != other.charge_percentage) {
      return false;
    }
    if (this->is_charging != other.is_charging) {
      return false;
    }
    return true;
  }
  bool operator!=(const BatteryStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BatteryStatus_

// alias to use template instance with default allocator
using BatteryStatus =
  roomie_msgs::msg::BatteryStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_HPP_
