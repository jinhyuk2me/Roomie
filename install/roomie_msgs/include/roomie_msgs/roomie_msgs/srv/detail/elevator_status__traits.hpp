// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from roomie_msgs:srv/ElevatorStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/elevator_status.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__ELEVATOR_STATUS__TRAITS_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__ELEVATOR_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "roomie_msgs/srv/detail/elevator_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ElevatorStatus_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ElevatorStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ElevatorStatus_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace roomie_msgs

namespace rosidl_generator_traits
{

[[deprecated("use roomie_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const roomie_msgs::srv::ElevatorStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ElevatorStatus_Request & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ElevatorStatus_Request>()
{
  return "roomie_msgs::srv::ElevatorStatus_Request";
}

template<>
inline const char * name<roomie_msgs::srv::ElevatorStatus_Request>()
{
  return "roomie_msgs/srv/ElevatorStatus_Request";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ElevatorStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ElevatorStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<roomie_msgs::srv::ElevatorStatus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ElevatorStatus_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: direction
  {
    out << "direction: ";
    rosidl_generator_traits::value_to_yaml(msg.direction, out);
    out << ", ";
  }

  // member: position
  {
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ElevatorStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << "\n";
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: direction
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction: ";
    rosidl_generator_traits::value_to_yaml(msg.direction, out);
    out << "\n";
  }

  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ElevatorStatus_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace roomie_msgs

namespace rosidl_generator_traits
{

[[deprecated("use roomie_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const roomie_msgs::srv::ElevatorStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ElevatorStatus_Response & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ElevatorStatus_Response>()
{
  return "roomie_msgs::srv::ElevatorStatus_Response";
}

template<>
inline const char * name<roomie_msgs::srv::ElevatorStatus_Response>()
{
  return "roomie_msgs/srv/ElevatorStatus_Response";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ElevatorStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ElevatorStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<roomie_msgs::srv::ElevatorStatus_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ElevatorStatus_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ElevatorStatus_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ElevatorStatus_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace roomie_msgs

namespace rosidl_generator_traits
{

[[deprecated("use roomie_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const roomie_msgs::srv::ElevatorStatus_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ElevatorStatus_Event & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ElevatorStatus_Event>()
{
  return "roomie_msgs::srv::ElevatorStatus_Event";
}

template<>
inline const char * name<roomie_msgs::srv::ElevatorStatus_Event>()
{
  return "roomie_msgs/srv/ElevatorStatus_Event";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ElevatorStatus_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ElevatorStatus_Event>
  : std::integral_constant<bool, has_bounded_size<roomie_msgs::srv::ElevatorStatus_Request>::value && has_bounded_size<roomie_msgs::srv::ElevatorStatus_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<roomie_msgs::srv::ElevatorStatus_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<roomie_msgs::srv::ElevatorStatus>()
{
  return "roomie_msgs::srv::ElevatorStatus";
}

template<>
inline const char * name<roomie_msgs::srv::ElevatorStatus>()
{
  return "roomie_msgs/srv/ElevatorStatus";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ElevatorStatus>
  : std::integral_constant<
    bool,
    has_fixed_size<roomie_msgs::srv::ElevatorStatus_Request>::value &&
    has_fixed_size<roomie_msgs::srv::ElevatorStatus_Response>::value
  >
{
};

template<>
struct has_bounded_size<roomie_msgs::srv::ElevatorStatus>
  : std::integral_constant<
    bool,
    has_bounded_size<roomie_msgs::srv::ElevatorStatus_Request>::value &&
    has_bounded_size<roomie_msgs::srv::ElevatorStatus_Response>::value
  >
{
};

template<>
struct is_service<roomie_msgs::srv::ElevatorStatus>
  : std::true_type
{
};

template<>
struct is_service_request<roomie_msgs::srv::ElevatorStatus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<roomie_msgs::srv::ElevatorStatus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROOMIE_MSGS__SRV__DETAIL__ELEVATOR_STATUS__TRAITS_HPP_
