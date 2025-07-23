// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/battery_status.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/BatteryStatus in the package roomie_msgs.
/**
  * BatteryStatus.msg
 */
typedef struct roomie_msgs__msg__BatteryStatus
{
  int32_t robot_id;
  float charge_percentage;
  bool is_charging;
} roomie_msgs__msg__BatteryStatus;

// Struct for a sequence of roomie_msgs__msg__BatteryStatus.
typedef struct roomie_msgs__msg__BatteryStatus__Sequence
{
  roomie_msgs__msg__BatteryStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__BatteryStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_
