// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from roomie_msgs:msg/Arrival.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/arrival.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__TRAITS_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "roomie_msgs/msg/detail/arrival__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace roomie_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Arrival & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: task_id
  {
    out << "task_id: ";
    rosidl_generator_traits::value_to_yaml(msg.task_id, out);
    out << ", ";
  }

  // member: location_id
  {
    out << "location_id: ";
    rosidl_generator_traits::value_to_yaml(msg.location_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Arrival & msg,
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

  // member: task_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_id: ";
    rosidl_generator_traits::value_to_yaml(msg.task_id, out);
    out << "\n";
  }

  // member: location_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "location_id: ";
    rosidl_generator_traits::value_to_yaml(msg.location_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Arrival & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace roomie_msgs

namespace rosidl_generator_traits
{

[[deprecated("use roomie_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const roomie_msgs::msg::Arrival & msg,
  std::ostream & out, size_t indentation = 0)
{
  roomie_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use roomie_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const roomie_msgs::msg::Arrival & msg)
{
  return roomie_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<roomie_msgs::msg::Arrival>()
{
  return "roomie_msgs::msg::Arrival";
}

template<>
inline const char * name<roomie_msgs::msg::Arrival>()
{
  return "roomie_msgs/msg/Arrival";
}

template<>
struct has_fixed_size<roomie_msgs::msg::Arrival>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<roomie_msgs::msg::Arrival>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<roomie_msgs::msg::Arrival>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__TRAITS_HPP_
