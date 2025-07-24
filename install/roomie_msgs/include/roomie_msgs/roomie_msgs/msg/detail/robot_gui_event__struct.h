// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/RobotGuiEvent.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/robot_gui_event.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'detail'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RobotGuiEvent in the package roomie_msgs.
/**
  * RobotGuiEvent.msg
 */
typedef struct roomie_msgs__msg__RobotGuiEvent
{
  int32_t robot_id;
  int32_t rgui_event_id;
  int32_t task_id;
  builtin_interfaces__msg__Time timestamp;
  rosidl_runtime_c__String detail;
} roomie_msgs__msg__RobotGuiEvent;

// Struct for a sequence of roomie_msgs__msg__RobotGuiEvent.
typedef struct roomie_msgs__msg__RobotGuiEvent__Sequence
{
  roomie_msgs__msg__RobotGuiEvent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__RobotGuiEvent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__STRUCT_H_
