// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/RoomiePose.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/roomie_pose.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/roomie_pose__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_RoomiePose_pose
{
public:
  explicit Init_RoomiePose_pose(::roomie_msgs::msg::RoomiePose & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::RoomiePose pose(::roomie_msgs::msg::RoomiePose::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::RoomiePose msg_;
};

class Init_RoomiePose_floor
{
public:
  explicit Init_RoomiePose_floor(::roomie_msgs::msg::RoomiePose & msg)
  : msg_(msg)
  {}
  Init_RoomiePose_pose floor(::roomie_msgs::msg::RoomiePose::_floor_type arg)
  {
    msg_.floor = std::move(arg);
    return Init_RoomiePose_pose(msg_);
  }

private:
  ::roomie_msgs::msg::RoomiePose msg_;
};

class Init_RoomiePose_robot_id
{
public:
  Init_RoomiePose_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RoomiePose_floor robot_id(::roomie_msgs::msg::RoomiePose::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_RoomiePose_floor(msg_);
  }

private:
  ::roomie_msgs::msg::RoomiePose msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::RoomiePose>()
{
  return roomie_msgs::msg::builder::Init_RoomiePose_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__BUILDER_HPP_
