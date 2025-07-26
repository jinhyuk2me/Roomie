// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from roomie_msgs:srv/SpaceAvailability.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/space_availability.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__SPACE_AVAILABILITY__TRAITS_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__SPACE_AVAILABILITY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "roomie_msgs/srv/detail/space_availability__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpaceAvailability_Request & msg,
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
  const SpaceAvailability_Request & msg,
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

inline std::string to_yaml(const SpaceAvailability_Request & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::SpaceAvailability_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::SpaceAvailability_Request & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::SpaceAvailability_Request>()
{
  return "roomie_msgs::srv::SpaceAvailability_Request";
}

template<>
inline const char * name<roomie_msgs::srv::SpaceAvailability_Request>()
{
  return "roomie_msgs/srv/SpaceAvailability_Request";
}

template<>
struct has_fixed_size<roomie_msgs::srv::SpaceAvailability_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<roomie_msgs::srv::SpaceAvailability_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<roomie_msgs::srv::SpaceAvailability_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SpaceAvailability_Response & msg,
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

  // member: space_availability
  {
    out << "space_availability: ";
    rosidl_generator_traits::value_to_yaml(msg.space_availability, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SpaceAvailability_Response & msg,
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

  // member: space_availability
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "space_availability: ";
    rosidl_generator_traits::value_to_yaml(msg.space_availability, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SpaceAvailability_Response & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::SpaceAvailability_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::SpaceAvailability_Response & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::SpaceAvailability_Response>()
{
  return "roomie_msgs::srv::SpaceAvailability_Response";
}

template<>
inline const char * name<roomie_msgs::srv::SpaceAvailability_Response>()
{
  return "roomie_msgs/srv/SpaceAvailability_Response";
}

template<>
struct has_fixed_size<roomie_msgs::srv::SpaceAvailability_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<roomie_msgs::srv::SpaceAvailability_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<roomie_msgs::srv::SpaceAvailability_Response>
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
  const SpaceAvailability_Event & msg,
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
  const SpaceAvailability_Event & msg,
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

inline std::string to_yaml(const SpaceAvailability_Event & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::SpaceAvailability_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::SpaceAvailability_Event & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::SpaceAvailability_Event>()
{
  return "roomie_msgs::srv::SpaceAvailability_Event";
}

template<>
inline const char * name<roomie_msgs::srv::SpaceAvailability_Event>()
{
  return "roomie_msgs/srv/SpaceAvailability_Event";
}

template<>
struct has_fixed_size<roomie_msgs::srv::SpaceAvailability_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roomie_msgs::srv::SpaceAvailability_Event>
  : std::integral_constant<bool, has_bounded_size<roomie_msgs::srv::SpaceAvailability_Request>::value && has_bounded_size<roomie_msgs::srv::SpaceAvailability_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<roomie_msgs::srv::SpaceAvailability_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<roomie_msgs::srv::SpaceAvailability>()
{
  return "roomie_msgs::srv::SpaceAvailability";
}

template<>
inline const char * name<roomie_msgs::srv::SpaceAvailability>()
{
  return "roomie_msgs/srv/SpaceAvailability";
}

template<>
struct has_fixed_size<roomie_msgs::srv::SpaceAvailability>
  : std::integral_constant<
    bool,
    has_fixed_size<roomie_msgs::srv::SpaceAvailability_Request>::value &&
    has_fixed_size<roomie_msgs::srv::SpaceAvailability_Response>::value
  >
{
};

template<>
struct has_bounded_size<roomie_msgs::srv::SpaceAvailability>
  : std::integral_constant<
    bool,
    has_bounded_size<roomie_msgs::srv::SpaceAvailability_Request>::value &&
    has_bounded_size<roomie_msgs::srv::SpaceAvailability_Response>::value
  >
{
};

template<>
struct is_service<roomie_msgs::srv::SpaceAvailability>
  : std::true_type
{
};

template<>
struct is_service_request<roomie_msgs::srv::SpaceAvailability_Request>
  : std::true_type
{
};

template<>
struct is_service_response<roomie_msgs::srv::SpaceAvailability_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROOMIE_MSGS__SRV__DETAIL__SPACE_AVAILABILITY__TRAITS_HPP_
