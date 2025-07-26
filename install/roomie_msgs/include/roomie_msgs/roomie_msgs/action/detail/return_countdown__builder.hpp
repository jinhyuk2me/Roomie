// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:action/ReturnCountdown.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/action/return_countdown.hpp"


#ifndef ROOMIE_MSGS__ACTION__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_
#define ROOMIE_MSGS__ACTION__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/action/detail/return_countdown__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_Goal_robot_id
{
public:
  Init_ReturnCountdown_Goal_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::action::ReturnCountdown_Goal robot_id(::roomie_msgs::action::ReturnCountdown_Goal::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_Goal>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_Goal_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_Result_success
{
public:
  explicit Init_ReturnCountdown_Result_success(::roomie_msgs::action::ReturnCountdown_Result & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_Result success(::roomie_msgs::action::ReturnCountdown_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_Result msg_;
};

class Init_ReturnCountdown_Result_robot_id
{
public:
  Init_ReturnCountdown_Result_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_Result_success robot_id(::roomie_msgs::action::ReturnCountdown_Result::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ReturnCountdown_Result_success(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_Result>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_Result_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_Feedback_remaining_time
{
public:
  Init_ReturnCountdown_Feedback_remaining_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::action::ReturnCountdown_Feedback remaining_time(::roomie_msgs::action::ReturnCountdown_Feedback::_remaining_time_type arg)
  {
    msg_.remaining_time = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_Feedback>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_Feedback_remaining_time();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_SendGoal_Request_goal
{
public:
  explicit Init_ReturnCountdown_SendGoal_Request_goal(::roomie_msgs::action::ReturnCountdown_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Request goal(::roomie_msgs::action::ReturnCountdown_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Request msg_;
};

class Init_ReturnCountdown_SendGoal_Request_goal_id
{
public:
  Init_ReturnCountdown_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_SendGoal_Request_goal goal_id(::roomie_msgs::action::ReturnCountdown_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_ReturnCountdown_SendGoal_Request_goal(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_SendGoal_Request>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_SendGoal_Request_goal_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_SendGoal_Response_stamp
{
public:
  explicit Init_ReturnCountdown_SendGoal_Response_stamp(::roomie_msgs::action::ReturnCountdown_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Response stamp(::roomie_msgs::action::ReturnCountdown_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Response msg_;
};

class Init_ReturnCountdown_SendGoal_Response_accepted
{
public:
  Init_ReturnCountdown_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_SendGoal_Response_stamp accepted(::roomie_msgs::action::ReturnCountdown_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_ReturnCountdown_SendGoal_Response_stamp(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_SendGoal_Response>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_SendGoal_Response_accepted();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_SendGoal_Event_response
{
public:
  explicit Init_ReturnCountdown_SendGoal_Event_response(::roomie_msgs::action::ReturnCountdown_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Event response(::roomie_msgs::action::ReturnCountdown_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Event msg_;
};

class Init_ReturnCountdown_SendGoal_Event_request
{
public:
  explicit Init_ReturnCountdown_SendGoal_Event_request(::roomie_msgs::action::ReturnCountdown_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_ReturnCountdown_SendGoal_Event_response request(::roomie_msgs::action::ReturnCountdown_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ReturnCountdown_SendGoal_Event_response(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Event msg_;
};

class Init_ReturnCountdown_SendGoal_Event_info
{
public:
  Init_ReturnCountdown_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_SendGoal_Event_request info(::roomie_msgs::action::ReturnCountdown_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ReturnCountdown_SendGoal_Event_request(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_SendGoal_Event>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_SendGoal_Event_info();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_GetResult_Request_goal_id
{
public:
  Init_ReturnCountdown_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::action::ReturnCountdown_GetResult_Request goal_id(::roomie_msgs::action::ReturnCountdown_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_GetResult_Request>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_GetResult_Request_goal_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_GetResult_Response_result
{
public:
  explicit Init_ReturnCountdown_GetResult_Response_result(::roomie_msgs::action::ReturnCountdown_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_GetResult_Response result(::roomie_msgs::action::ReturnCountdown_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Response msg_;
};

class Init_ReturnCountdown_GetResult_Response_status
{
public:
  Init_ReturnCountdown_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_GetResult_Response_result status(::roomie_msgs::action::ReturnCountdown_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_ReturnCountdown_GetResult_Response_result(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_GetResult_Response>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_GetResult_Response_status();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_GetResult_Event_response
{
public:
  explicit Init_ReturnCountdown_GetResult_Event_response(::roomie_msgs::action::ReturnCountdown_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_GetResult_Event response(::roomie_msgs::action::ReturnCountdown_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Event msg_;
};

class Init_ReturnCountdown_GetResult_Event_request
{
public:
  explicit Init_ReturnCountdown_GetResult_Event_request(::roomie_msgs::action::ReturnCountdown_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_ReturnCountdown_GetResult_Event_response request(::roomie_msgs::action::ReturnCountdown_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ReturnCountdown_GetResult_Event_response(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Event msg_;
};

class Init_ReturnCountdown_GetResult_Event_info
{
public:
  Init_ReturnCountdown_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_GetResult_Event_request info(::roomie_msgs::action::ReturnCountdown_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ReturnCountdown_GetResult_Event_request(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_GetResult_Event>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_GetResult_Event_info();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace action
{

namespace builder
{

class Init_ReturnCountdown_FeedbackMessage_feedback
{
public:
  explicit Init_ReturnCountdown_FeedbackMessage_feedback(::roomie_msgs::action::ReturnCountdown_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::action::ReturnCountdown_FeedbackMessage feedback(::roomie_msgs::action::ReturnCountdown_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_FeedbackMessage msg_;
};

class Init_ReturnCountdown_FeedbackMessage_goal_id
{
public:
  Init_ReturnCountdown_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReturnCountdown_FeedbackMessage_feedback goal_id(::roomie_msgs::action::ReturnCountdown_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_ReturnCountdown_FeedbackMessage_feedback(msg_);
  }

private:
  ::roomie_msgs::action::ReturnCountdown_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::action::ReturnCountdown_FeedbackMessage>()
{
  return roomie_msgs::action::builder::Init_ReturnCountdown_FeedbackMessage_goal_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__ACTION__DETAIL__RETURN_COUNTDOWN__BUILDER_HPP_
