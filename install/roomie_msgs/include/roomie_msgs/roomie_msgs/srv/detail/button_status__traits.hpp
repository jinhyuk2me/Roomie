// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from roomie_msgs:srv/ButtonStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/button_status.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__TRAITS_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "roomie_msgs/srv/detail/button_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ButtonStatus_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: button_ids
  {
    if (msg.button_ids.size() == 0) {
      out << "button_ids: []";
    } else {
      out << "button_ids: [";
      size_t pending_items = msg.button_ids.size();
      for (auto item : msg.button_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const ButtonStatus_Request & msg,
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

  // member: button_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.button_ids.size() == 0) {
      out << "button_ids: []\n";
    } else {
      out << "button_ids:\n";
      for (auto item : msg.button_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ButtonStatus_Request & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::ButtonStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ButtonStatus_Request & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ButtonStatus_Request>()
{
  return "roomie_msgs::srv::ButtonStatus_Request";
}

template<>
inline const char * name<roomie_msgs::srv::ButtonStatus_Request>()
{
  return "roomie_msgs/srv/ButtonStatus_Request";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ButtonStatus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ButtonStatus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<roomie_msgs::srv::ButtonStatus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace roomie_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ButtonStatus_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: xs
  {
    if (msg.xs.size() == 0) {
      out << "xs: []";
    } else {
      out << "xs: [";
      size_t pending_items = msg.xs.size();
      for (auto item : msg.xs) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: ys
  {
    if (msg.ys.size() == 0) {
      out << "ys: []";
    } else {
      out << "ys: [";
      size_t pending_items = msg.ys.size();
      for (auto item : msg.ys) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: depths
  {
    if (msg.depths.size() == 0) {
      out << "depths: []";
    } else {
      out << "depths: [";
      size_t pending_items = msg.depths.size();
      for (auto item : msg.depths) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: is_pressed
  {
    if (msg.is_pressed.size() == 0) {
      out << "is_pressed: []";
    } else {
      out << "is_pressed: [";
      size_t pending_items = msg.is_pressed.size();
      for (auto item : msg.is_pressed) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: timestamp
  {
    if (msg.timestamp.size() == 0) {
      out << "timestamp: []";
    } else {
      out << "timestamp: [";
      size_t pending_items = msg.timestamp.size();
      for (auto item : msg.timestamp) {
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
  const ButtonStatus_Response & msg,
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

  // member: xs
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.xs.size() == 0) {
      out << "xs: []\n";
    } else {
      out << "xs:\n";
      for (auto item : msg.xs) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: ys
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ys.size() == 0) {
      out << "ys: []\n";
    } else {
      out << "ys:\n";
      for (auto item : msg.ys) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: depths
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.depths.size() == 0) {
      out << "depths: []\n";
    } else {
      out << "depths:\n";
      for (auto item : msg.depths) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: is_pressed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.is_pressed.size() == 0) {
      out << "is_pressed: []\n";
    } else {
      out << "is_pressed:\n";
      for (auto item : msg.is_pressed) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.timestamp.size() == 0) {
      out << "timestamp: []\n";
    } else {
      out << "timestamp:\n";
      for (auto item : msg.timestamp) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ButtonStatus_Response & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::ButtonStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ButtonStatus_Response & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ButtonStatus_Response>()
{
  return "roomie_msgs::srv::ButtonStatus_Response";
}

template<>
inline const char * name<roomie_msgs::srv::ButtonStatus_Response>()
{
  return "roomie_msgs/srv/ButtonStatus_Response";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ButtonStatus_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ButtonStatus_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<roomie_msgs::srv::ButtonStatus_Response>
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
  const ButtonStatus_Event & msg,
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
  const ButtonStatus_Event & msg,
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

inline std::string to_yaml(const ButtonStatus_Event & msg, bool use_flow_style = false)
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
  const roomie_msgs::srv::ButtonStatus_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::srv::ButtonStatus_Event & msg)
{
  return roomie_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::srv::ButtonStatus_Event>()
{
  return "roomie_msgs::srv::ButtonStatus_Event";
}

template<>
inline const char * name<roomie_msgs::srv::ButtonStatus_Event>()
{
  return "roomie_msgs/srv/ButtonStatus_Event";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ButtonStatus_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<roomie_msgs::srv::ButtonStatus_Event>
  : std::integral_constant<bool, has_bounded_size<roomie_msgs::srv::ButtonStatus_Request>::value && has_bounded_size<roomie_msgs::srv::ButtonStatus_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<roomie_msgs::srv::ButtonStatus_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<roomie_msgs::srv::ButtonStatus>()
{
  return "roomie_msgs::srv::ButtonStatus";
}

template<>
inline const char * name<roomie_msgs::srv::ButtonStatus>()
{
  return "roomie_msgs/srv/ButtonStatus";
}

template<>
struct has_fixed_size<roomie_msgs::srv::ButtonStatus>
  : std::integral_constant<
    bool,
    has_fixed_size<roomie_msgs::srv::ButtonStatus_Request>::value &&
    has_fixed_size<roomie_msgs::srv::ButtonStatus_Response>::value
  >
{
};

template<>
struct has_bounded_size<roomie_msgs::srv::ButtonStatus>
  : std::integral_constant<
    bool,
    has_bounded_size<roomie_msgs::srv::ButtonStatus_Request>::value &&
    has_bounded_size<roomie_msgs::srv::ButtonStatus_Response>::value
  >
{
};

template<>
struct is_service<roomie_msgs::srv::ButtonStatus>
  : std::true_type
{
};

template<>
struct is_service_request<roomie_msgs::srv::ButtonStatus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<roomie_msgs::srv::ButtonStatus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__TRAITS_HPP_
