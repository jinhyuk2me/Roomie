// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/CheckDoorState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/check_door_state.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__CHECK_DOOR_STATE__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__CHECK_DOOR_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/check_door_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckDoorState_Request_robot_id
{
public:
  Init_CheckDoorState_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::srv::CheckDoorState_Request robot_id(::roomie_msgs::srv::CheckDoorState_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckDoorState_Request>()
{
  return roomie_msgs::srv::builder::Init_CheckDoorState_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckDoorState_Response_is_opened
{
public:
  explicit Init_CheckDoorState_Response_is_opened(::roomie_msgs::srv::CheckDoorState_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CheckDoorState_Response is_opened(::roomie_msgs::srv::CheckDoorState_Response::_is_opened_type arg)
  {
    msg_.is_opened = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Response msg_;
};

class Init_CheckDoorState_Response_robot_id
{
public:
  Init_CheckDoorState_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CheckDoorState_Response_is_opened robot_id(::roomie_msgs::srv::CheckDoorState_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_CheckDoorState_Response_is_opened(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckDoorState_Response>()
{
  return roomie_msgs::srv::builder::Init_CheckDoorState_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckDoorState_Event_response
{
public:
  explicit Init_CheckDoorState_Event_response(::roomie_msgs::srv::CheckDoorState_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CheckDoorState_Event response(::roomie_msgs::srv::CheckDoorState_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Event msg_;
};

class Init_CheckDoorState_Event_request
{
public:
  explicit Init_CheckDoorState_Event_request(::roomie_msgs::srv::CheckDoorState_Event & msg)
  : msg_(msg)
  {}
  Init_CheckDoorState_Event_response request(::roomie_msgs::srv::CheckDoorState_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_CheckDoorState_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Event msg_;
};

class Init_CheckDoorState_Event_info
{
public:
  Init_CheckDoorState_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CheckDoorState_Event_request info(::roomie_msgs::srv::CheckDoorState_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_CheckDoorState_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::CheckDoorState_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckDoorState_Event>()
{
  return roomie_msgs::srv::builder::Init_CheckDoorState_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__CHECK_DOOR_STATE__BUILDER_HPP_
