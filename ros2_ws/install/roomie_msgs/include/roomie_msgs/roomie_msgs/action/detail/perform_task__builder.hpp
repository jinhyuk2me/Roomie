// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:action/PerformTask.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/action/perform_task.hpp"


#ifndef ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__BUILDER_HPP_
#define ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/action/detail/perform_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_Goal_order_info
{
public:
  explicit Init_PerformTask_Goal_order_info(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_Goal order_info(::roomie_msgs::action::PerformTask_Goal::_order_info_type arg)
  {
    msg_.order_info = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_pickup_location_id
{
public:
  explicit Init_PerformTask_Goal_pickup_location_id(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Goal_order_info pickup_location_id(::roomie_msgs::action::PerformTask_Goal::_pickup_location_id_type arg)
  {
    msg_.pickup_location_id = std::move(arg);
    return Init_PerformTask_Goal_order_info(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_target_location_id
{
public:
  explicit Init_PerformTask_Goal_target_location_id(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Goal_pickup_location_id target_location_id(::roomie_msgs::action::PerformTask_Goal::_target_location_id_type arg)
  {
    msg_.target_location_id = std::move(arg);
    return Init_PerformTask_Goal_pickup_location_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_task_status_id
{
public:
  explicit Init_PerformTask_Goal_task_status_id(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Goal_target_location_id task_status_id(::roomie_msgs::action::PerformTask_Goal::_task_status_id_type arg)
  {
    msg_.task_status_id = std::move(arg);
    return Init_PerformTask_Goal_target_location_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_task_type_id
{
public:
  explicit Init_PerformTask_Goal_task_type_id(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Goal_task_status_id task_type_id(::roomie_msgs::action::PerformTask_Goal::_task_type_id_type arg)
  {
    msg_.task_type_id = std::move(arg);
    return Init_PerformTask_Goal_task_status_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_task_id
{
public:
  explicit Init_PerformTask_Goal_task_id(::roomie_msgs::action::PerformTask_Goal & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Goal_task_type_id task_id(::roomie_msgs::action::PerformTask_Goal::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_PerformTask_Goal_task_type_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

class Init_PerformTask_Goal_robot_id
{
public:
  Init_PerformTask_Goal_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_Goal_task_id robot_id(::roomie_msgs::action::PerformTask_Goal::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_PerformTask_Goal_task_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_Goal>()
{
  return roomie_msgs::action::builder::Init_PerformTask_Goal_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_Result_message
{
public:
  explicit Init_PerformTask_Result_message(::roomie_msgs::action::PerformTask_Result & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_Result message(::roomie_msgs::action::PerformTask_Result::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Result msg_;
};

class Init_PerformTask_Result_success
{
public:
  explicit Init_PerformTask_Result_success(::roomie_msgs::action::PerformTask_Result & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Result_message success(::roomie_msgs::action::PerformTask_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_PerformTask_Result_message(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Result msg_;
};

class Init_PerformTask_Result_task_id
{
public:
  explicit Init_PerformTask_Result_task_id(::roomie_msgs::action::PerformTask_Result & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Result_success task_id(::roomie_msgs::action::PerformTask_Result::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_PerformTask_Result_success(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Result msg_;
};

class Init_PerformTask_Result_robot_id
{
public:
  Init_PerformTask_Result_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_Result_task_id robot_id(::roomie_msgs::action::PerformTask_Result::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_PerformTask_Result_task_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_Result>()
{
  return roomie_msgs::action::builder::Init_PerformTask_Result_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_Feedback_task_status_id
{
public:
  explicit Init_PerformTask_Feedback_task_status_id(::roomie_msgs::action::PerformTask_Feedback & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_Feedback task_status_id(::roomie_msgs::action::PerformTask_Feedback::_task_status_id_type arg)
  {
    msg_.task_status_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Feedback msg_;
};

class Init_PerformTask_Feedback_task_id
{
public:
  explicit Init_PerformTask_Feedback_task_id(::roomie_msgs::action::PerformTask_Feedback & msg)
  : msg_(msg)
  {}
  Init_PerformTask_Feedback_task_status_id task_id(::roomie_msgs::action::PerformTask_Feedback::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_PerformTask_Feedback_task_status_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Feedback msg_;
};

class Init_PerformTask_Feedback_robot_id
{
public:
  Init_PerformTask_Feedback_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_Feedback_task_id robot_id(::roomie_msgs::action::PerformTask_Feedback::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_PerformTask_Feedback_task_id(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_Feedback>()
{
  return roomie_msgs::action::builder::Init_PerformTask_Feedback_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_SendGoal_Request_goal
{
public:
  explicit Init_PerformTask_SendGoal_Request_goal(::roomie_msgs::action::PerformTask_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_SendGoal_Request goal(::roomie_msgs::action::PerformTask_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Request msg_;
};

class Init_PerformTask_SendGoal_Request_goal_id
{
public:
  Init_PerformTask_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_SendGoal_Request_goal goal_id(::roomie_msgs::action::PerformTask_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_PerformTask_SendGoal_Request_goal(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_SendGoal_Request>()
{
  return roomie_msgs::action::builder::Init_PerformTask_SendGoal_Request_goal_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_SendGoal_Response_stamp
{
public:
  explicit Init_PerformTask_SendGoal_Response_stamp(::roomie_msgs::action::PerformTask_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_SendGoal_Response stamp(::roomie_msgs::action::PerformTask_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Response msg_;
};

class Init_PerformTask_SendGoal_Response_accepted
{
public:
  Init_PerformTask_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_SendGoal_Response_stamp accepted(::roomie_msgs::action::PerformTask_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_PerformTask_SendGoal_Response_stamp(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_SendGoal_Response>()
{
  return roomie_msgs::action::builder::Init_PerformTask_SendGoal_Response_accepted();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_SendGoal_Event_response
{
public:
  explicit Init_PerformTask_SendGoal_Event_response(::roomie_msgs::action::PerformTask_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_SendGoal_Event response(::roomie_msgs::action::PerformTask_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Event msg_;
};

class Init_PerformTask_SendGoal_Event_request
{
public:
  explicit Init_PerformTask_SendGoal_Event_request(::roomie_msgs::action::PerformTask_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_PerformTask_SendGoal_Event_response request(::roomie_msgs::action::PerformTask_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_PerformTask_SendGoal_Event_response(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Event msg_;
};

class Init_PerformTask_SendGoal_Event_info
{
public:
  Init_PerformTask_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_SendGoal_Event_request info(::roomie_msgs::action::PerformTask_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_PerformTask_SendGoal_Event_request(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_SendGoal_Event>()
{
  return roomie_msgs::action::builder::Init_PerformTask_SendGoal_Event_info();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_GetResult_Request_goal_id
{
public:
  Init_PerformTask_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::action::PerformTask_GetResult_Request goal_id(::roomie_msgs::action::PerformTask_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_GetResult_Request>()
{
  return roomie_msgs::action::builder::Init_PerformTask_GetResult_Request_goal_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_GetResult_Response_result
{
public:
  explicit Init_PerformTask_GetResult_Response_result(::roomie_msgs::action::PerformTask_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_GetResult_Response result(::roomie_msgs::action::PerformTask_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Response msg_;
};

class Init_PerformTask_GetResult_Response_status
{
public:
  Init_PerformTask_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_GetResult_Response_result status(::roomie_msgs::action::PerformTask_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_PerformTask_GetResult_Response_result(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_GetResult_Response>()
{
  return roomie_msgs::action::builder::Init_PerformTask_GetResult_Response_status();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_GetResult_Event_response
{
public:
  explicit Init_PerformTask_GetResult_Event_response(::roomie_msgs::action::PerformTask_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_GetResult_Event response(::roomie_msgs::action::PerformTask_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Event msg_;
};

class Init_PerformTask_GetResult_Event_request
{
public:
  explicit Init_PerformTask_GetResult_Event_request(::roomie_msgs::action::PerformTask_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_PerformTask_GetResult_Event_response request(::roomie_msgs::action::PerformTask_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_PerformTask_GetResult_Event_response(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Event msg_;
};

class Init_PerformTask_GetResult_Event_info
{
public:
  Init_PerformTask_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_GetResult_Event_request info(::roomie_msgs::action::PerformTask_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_PerformTask_GetResult_Event_request(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_GetResult_Event>()
{
  return roomie_msgs::action::builder::Init_PerformTask_GetResult_Event_info();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_PerformTask_FeedbackMessage_feedback
{
public:
  explicit Init_PerformTask_FeedbackMessage_feedback(::roomie_msgs::action::PerformTask_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::PerformTask_FeedbackMessage feedback(::roomie_msgs::action::PerformTask_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_FeedbackMessage msg_;
};

class Init_PerformTask_FeedbackMessage_goal_id
{
public:
  Init_PerformTask_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerformTask_FeedbackMessage_feedback goal_id(::roomie_msgs::action::PerformTask_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_PerformTask_FeedbackMessage_feedback(msg_);
  }

private:
  ::roomie_msgs::action::PerformTask_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::PerformTask_FeedbackMessage>()
{
  return roomie_msgs::action::builder::Init_PerformTask_FeedbackMessage_goal_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__BUILDER_HPP_
