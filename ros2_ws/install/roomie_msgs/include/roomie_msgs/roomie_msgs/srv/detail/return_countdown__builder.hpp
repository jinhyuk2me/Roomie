// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/ReturnCountdown.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/return_countdown.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/return_countdown__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ReturnCountdown_Request_robot_id
{
public:
  Init_ReturnCountdown_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::srv::ReturnCountdown_Request robot_id(::roomie_msgs::srv::ReturnCountdown_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ReturnCountdown_Request>()
{
  return roomie_msgs::srv::builder::Init_ReturnCountdown_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ReturnCountdown_Response_reason
{
public:
  explicit Init_ReturnCountdown_Response_reason(::roomie_msgs::srv::ReturnCountdown_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ReturnCountdown_Response reason(::roomie_msgs::srv::ReturnCountdown_Response::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Response msg_;
};

class Init_ReturnCountdown_Response_success
{
public:
  explicit Init_ReturnCountdown_Response_success(::roomie_msgs::srv::ReturnCountdown_Response & msg)
  : msg_(msg)
  {}
  Init_ReturnCountdown_Response_reason success(::roomie_msgs::srv::ReturnCountdown_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ReturnCountdown_Response_reason(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Response msg_;
};

class Init_ReturnCountdown_Response_robot_id
{
public:
  Init_ReturnCountdown_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_Response_success robot_id(::roomie_msgs::srv::ReturnCountdown_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ReturnCountdown_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ReturnCountdown_Response>()
{
  return roomie_msgs::srv::builder::Init_ReturnCountdown_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ReturnCountdown_Event_response
{
public:
  explicit Init_ReturnCountdown_Event_response(::roomie_msgs::srv::ReturnCountdown_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ReturnCountdown_Event response(::roomie_msgs::srv::ReturnCountdown_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Event msg_;
};

class Init_ReturnCountdown_Event_request
{
public:
  explicit Init_ReturnCountdown_Event_request(::roomie_msgs::srv::ReturnCountdown_Event & msg)
  : msg_(msg)
  {}
  Init_ReturnCountdown_Event_response request(::roomie_msgs::srv::ReturnCountdown_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ReturnCountdown_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Event msg_;
};

class Init_ReturnCountdown_Event_info
{
public:
  Init_ReturnCountdown_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_Event_request info(::roomie_msgs::srv::ReturnCountdown_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ReturnCountdown_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::ReturnCountdown_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ReturnCountdown_Event>()
{
  return roomie_msgs::srv::builder::Init_ReturnCountdown_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_
