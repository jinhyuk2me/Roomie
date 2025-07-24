// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/RoomiePose.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/roomie_pose.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in msg/RoomiePose in the package roomie_msgs.
/**
  * RoomiePose.msg
 */
typedef struct roomie_msgs__msg__RoomiePose
{
  int32_t robot_id;
  int32_t floor;
  geometry_msgs__msg__Pose pose;
} roomie_msgs__msg__RoomiePose;

// Struct for a sequence of roomie_msgs__msg__RoomiePose.
typedef struct roomie_msgs__msg__RoomiePose__Sequence
{
  roomie_msgs__msg__RoomiePose * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__RoomiePose__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROOMIE_POSE__STRUCT_H_
