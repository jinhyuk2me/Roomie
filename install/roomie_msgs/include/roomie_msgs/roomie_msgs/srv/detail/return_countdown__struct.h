// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:srv/ReturnCountdown.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/return_countdown.h"


#ifndef ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__STRUCT_H_
#define ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ReturnCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__ReturnCountdown_Request
{
  int32_t robot_id;
} roomie_msgs__srv__ReturnCountdown_Request;

// Struct for a sequence of roomie_msgs__srv__ReturnCountdown_Request.
typedef struct roomie_msgs__srv__ReturnCountdown_Request__Sequence
{
  roomie_msgs__srv__ReturnCountdown_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__ReturnCountdown_Request__Sequence;

// Constants defined in the message

/// Struct defined in srv/ReturnCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__ReturnCountdown_Response
{
  int32_t robot_id;
  bool success;
  int32_t reason;
} roomie_msgs__srv__ReturnCountdown_Response;

// Struct for a sequence of roomie_msgs__srv__ReturnCountdown_Response.
typedef struct roomie_msgs__srv__ReturnCountdown_Response__Sequence
{
  roomie_msgs__srv__ReturnCountdown_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__ReturnCountdown_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  roomie_msgs__srv__ReturnCountdown_Event__request__MAX_SIZE = 1
};
// response
enum
{
  roomie_msgs__srv__ReturnCountdown_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/ReturnCountdown in the package roomie_msgs.
typedef struct roomie_msgs__srv__ReturnCountdown_Event
{
  service_msgs__msg__ServiceEventInfo info;
  roomie_msgs__srv__ReturnCountdown_Request__Sequence request;
  roomie_msgs__srv__ReturnCountdown_Response__Sequence response;
} roomie_msgs__srv__ReturnCountdown_Event;

// Struct for a sequence of roomie_msgs__srv__ReturnCountdown_Event.
typedef struct roomie_msgs__srv__ReturnCountdown_Event__Sequence
{
  roomie_msgs__srv__ReturnCountdown_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__ReturnCountdown_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__SRV__DETAIL__RETURN_COUNTDOWN__STRUCT_H_
