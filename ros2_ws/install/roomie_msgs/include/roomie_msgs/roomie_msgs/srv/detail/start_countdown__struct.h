// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:srv/StartCountdown.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/start_countdown.h"


#ifndef ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__STRUCT_H_
#define ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/StartCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__StartCountdown_Request
{
  int32_t robot_id;
  int32_t task_id;
  int32_t task_type_id;
} roomie_msgs__srv__StartCountdown_Request;

// Struct for a sequence of roomie_msgs__srv__StartCountdown_Request.
typedef struct roomie_msgs__srv__StartCountdown_Request__Sequence
{
  roomie_msgs__srv__StartCountdown_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__StartCountdown_Request__Sequence;

// Constants defined in the message

/// Struct defined in srv/StartCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__StartCountdown_Response
{
  int32_t robot_id;
  bool success;
  int32_t reason;
} roomie_msgs__srv__StartCountdown_Response;

// Struct for a sequence of roomie_msgs__srv__StartCountdown_Response.
typedef struct roomie_msgs__srv__StartCountdown_Response__Sequence
{
  roomie_msgs__srv__StartCountdown_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__StartCountdown_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  roomie_msgs__srv__StartCountdown_Event__request__MAX_SIZE = 1
};
// response
enum
{
  roomie_msgs__srv__StartCountdown_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/StartCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__StartCountdown_Event
{
  service_msgs__msg__ServiceEventInfo info;
  roomie_msgs__srv__StartCountdown_Request__Sequence request;
  roomie_msgs__srv__StartCountdown_Response__Sequence response;
} roomie_msgs__srv__StartCountdown_Event;

// Struct for a sequence of roomie_msgs__srv__StartCountdown_Event.
typedef struct roomie_msgs__srv__StartCountdown_Event__Sequence
{
  roomie_msgs__srv__StartCountdown_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__StartCountdown_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__SRV__DETAIL__START_COUNTDOWN__STRUCT_H_
