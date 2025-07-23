// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/battery_status.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/battery_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_BatteryStatus_is_charging
{
public:
  explicit Init_BatteryStatus_is_charging(::roomie_msgs::msg::BatteryStatus & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::BatteryStatus is_charging(::roomie_msgs::msg::BatteryStatus::_is_charging_type arg)
  {
    msg_.is_charging = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::BatteryStatus msg_;
};

class Init_BatteryStatus_charge_percentage
{
public:
  explicit Init_BatteryStatus_charge_percentage(::roomie_msgs::msg::BatteryStatus & msg)
  : msg_(msg)
  {}
  Init_BatteryStatus_is_charging charge_percentage(::roomie_msgs::msg::BatteryStatus::_charge_percentage_type arg)
  {
    msg_.charge_percentage = std::move(arg);
    return Init_BatteryStatus_is_charging(msg_);
  }

private:
  ::roomie_msgs::msg::BatteryStatus msg_;
};

class Init_BatteryStatus_robot_id
{
public:
  Init_BatteryStatus_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BatteryStatus_charge_percentage robot_id(::roomie_msgs::msg::BatteryStatus::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_BatteryStatus_charge_percentage(msg_);
  }

private:
  ::roomie_msgs::msg::BatteryStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::BatteryStatus>()
{
  return roomie_msgs::msg::builder::Init_BatteryStatus_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_
