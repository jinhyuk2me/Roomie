// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/CreateTask.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/create_task.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__CREATE_TASK__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__CREATE_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/create_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CreateTask_Request_target_location_id
{
public:
  explicit Init_CreateTask_Request_target_location_id(::roomie_msgs::srv::CreateTask_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CreateTask_Request target_location_id(::roomie_msgs::srv::CreateTask_Request::_target_location_id_type arg)
  {
    msg_.target_location_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Request msg_;
};

class Init_CreateTask_Request_robot_id
{
public:
  Init_CreateTask_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CreateTask_Request_target_location_id robot_id(::roomie_msgs::srv::CreateTask_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_CreateTask_Request_target_location_id(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CreateTask_Request>()
{
  return roomie_msgs::srv::builder::Init_CreateTask_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CreateTask_Response_message
{
public:
  explicit Init_CreateTask_Response_message(::roomie_msgs::srv::CreateTask_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CreateTask_Response message(::roomie_msgs::srv::CreateTask_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Response msg_;
};

class Init_CreateTask_Response_success
{
public:
  explicit Init_CreateTask_Response_success(::roomie_msgs::srv::CreateTask_Response & msg)
  : msg_(msg)
  {}
  Init_CreateTask_Response_message success(::roomie_msgs::srv::CreateTask_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_CreateTask_Response_message(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Response msg_;
};

class Init_CreateTask_Response_task_id
{
public:
  explicit Init_CreateTask_Response_task_id(::roomie_msgs::srv::CreateTask_Response & msg)
  : msg_(msg)
  {}
  Init_CreateTask_Response_success task_id(::roomie_msgs::srv::CreateTask_Response::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_CreateTask_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Response msg_;
};

class Init_CreateTask_Response_robot_id
{
public:
  Init_CreateTask_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CreateTask_Response_task_id robot_id(::roomie_msgs::srv::CreateTask_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_CreateTask_Response_task_id(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CreateTask_Response>()
{
  return roomie_msgs::srv::builder::Init_CreateTask_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CreateTask_Event_response
{
public:
  explicit Init_CreateTask_Event_response(::roomie_msgs::srv::CreateTask_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CreateTask_Event response(::roomie_msgs::srv::CreateTask_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Event msg_;
};

class Init_CreateTask_Event_request
{
public:
  explicit Init_CreateTask_Event_request(::roomie_msgs::srv::CreateTask_Event & msg)
  : msg_(msg)
  {}
  Init_CreateTask_Event_response request(::roomie_msgs::srv::CreateTask_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_CreateTask_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Event msg_;
};

class Init_CreateTask_Event_info
{
public:
  Init_CreateTask_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CreateTask_Event_request info(::roomie_msgs::srv::CreateTask_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_CreateTask_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::CreateTask_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CreateTask_Event>()
{
  return roomie_msgs::srv::builder::Init_CreateTask_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__CREATE_TASK__BUILDER_HPP_
