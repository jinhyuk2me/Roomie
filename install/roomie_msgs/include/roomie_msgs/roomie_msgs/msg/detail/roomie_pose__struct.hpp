// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roomie_msgs:msg/RoomiePose.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/roomie_pose.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__msg__RoomiePose __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__msg__RoomiePose __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RoomiePose_
{
  using Type = RoomiePose_<ContainerAllocator>;

  explicit RoomiePose_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->floor_id = 0l;
    }
  }

  explicit RoomiePose_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->floor_id = 0l;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _floor_id_type =
    int32_t;
  _floor_id_type floor_id;
  using _pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _pose_type pose;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__floor_id(
    const int32_t & _arg)
  {
    this->floor_id = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::msg::RoomiePose_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::msg::RoomiePose_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::RoomiePose_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::msg::RoomiePose_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__msg__RoomiePose
    std::shared_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__msg__RoomiePose
    std::shared_ptr<roomie_msgs::msg::RoomiePose_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RoomiePose_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->floor_id != other.floor_id) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const RoomiePose_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RoomiePose_

// alias to use template instance with default allocator
using RoomiePose =
  roomie_msgs::msg::RoomiePose_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_HPP_
