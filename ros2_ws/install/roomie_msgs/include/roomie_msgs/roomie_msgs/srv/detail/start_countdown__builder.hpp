// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/StartCountdown.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/start_countdown.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/start_countdown__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_StartCountdown_Request_task_type_id
{
public:
  explicit Init_StartCountdown_Request_task_type_id(::roomie_msgs::srv::StartCountdown_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::StartCountdown_Request task_type_id(::roomie_msgs::srv::StartCountdown_Request::_task_type_id_type arg)
  {
    msg_.task_type_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Request msg_;
};

class Init_StartCountdown_Request_task_id
{
public:
  explicit Init_StartCountdown_Request_task_id(::roomie_msgs::srv::StartCountdown_Request & msg)
  : msg_(msg)
  {}
  Init_StartCountdown_Request_task_type_id task_id(::roomie_msgs::srv::StartCountdown_Request::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_StartCountdown_Request_task_type_id(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Request msg_;
};

class Init_StartCountdown_Request_robot_id
{
public:
  Init_StartCountdown_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartCountdown_Request_task_id robot_id(::roomie_msgs::srv::StartCountdown_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_StartCountdown_Request_task_id(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::StartCountdown_Request>()
{
  return roomie_msgs::srv::builder::Init_StartCountdown_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_StartCountdown_Response_reason
{
public:
  explicit Init_StartCountdown_Response_reason(::roomie_msgs::srv::StartCountdown_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::StartCountdown_Response reason(::roomie_msgs::srv::StartCountdown_Response::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Response msg_;
};

class Init_StartCountdown_Response_success
{
public:
  explicit Init_StartCountdown_Response_success(::roomie_msgs::srv::StartCountdown_Response & msg)
  : msg_(msg)
  {}
  Init_StartCountdown_Response_reason success(::roomie_msgs::srv::StartCountdown_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_StartCountdown_Response_reason(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Response msg_;
};

class Init_StartCountdown_Response_robot_id
{
public:
  Init_StartCountdown_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartCountdown_Response_success robot_id(::roomie_msgs::srv::StartCountdown_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_StartCountdown_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::StartCountdown_Response>()
{
  return roomie_msgs::srv::builder::Init_StartCountdown_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_StartCountdown_Event_response
{
public:
  explicit Init_StartCountdown_Event_response(::roomie_msgs::srv::StartCountdown_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::StartCountdown_Event response(::roomie_msgs::srv::StartCountdown_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Event msg_;
};

class Init_StartCountdown_Event_request
{
public:
  explicit Init_StartCountdown_Event_request(::roomie_msgs::srv::StartCountdown_Event & msg)
  : msg_(msg)
  {}
  Init_StartCountdown_Event_response request(::roomie_msgs::srv::StartCountdown_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_StartCountdown_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Event msg_;
};

class Init_StartCountdown_Event_info
{
public:
  Init_StartCountdown_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartCountdown_Event_request info(::roomie_msgs::srv::StartCountdown_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_StartCountdown_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::StartCountdown_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::StartCountdown_Event>()
{
  return roomie_msgs::srv::builder::Init_StartCountdown_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__BUILDER_HPP_
