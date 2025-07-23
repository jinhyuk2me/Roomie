// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:action/PerformTask.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/action/perform_task.h"


#ifndef ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_H_
#define ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'order_info'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_Goal
{
  int32_t robot_id;
  int32_t task_id;
  int32_t task_type_id;
  int32_t task_status_id;
  int32_t target_location_id;
  int32_t pickup_location_id;
  /// 주문 정보 (JSON)
  rosidl_runtime_c__String order_info;
} roomie_msgs__action__PerformTask_Goal;

// Struct for a sequence of roomie_msgs__action__PerformTask_Goal.
typedef struct roomie_msgs__action__PerformTask_Goal__Sequence
{
  roomie_msgs__action__PerformTask_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_Goal__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_Result
{
  int32_t robot_id;
  int32_t task_id;
  bool success;
  rosidl_runtime_c__String message;
} roomie_msgs__action__PerformTask_Result;

// Struct for a sequence of roomie_msgs__action__PerformTask_Result.
typedef struct roomie_msgs__action__PerformTask_Result__Sequence
{
  roomie_msgs__action__PerformTask_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_Result__Sequence;

// Constants defined in the message

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_Feedback
{
  int32_t robot_id;
  int32_t task_id;
  int32_t task_status_id;
} roomie_msgs__action__PerformTask_Feedback;

// Struct for a sequence of roomie_msgs__action__PerformTask_Feedback.
typedef struct roomie_msgs__action__PerformTask_Feedback__Sequence
{
  roomie_msgs__action__PerformTask_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_Feedback__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "roomie_msgs/action/detail/perform_task__struct.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  roomie_msgs__action__PerformTask_Goal goal;
} roomie_msgs__action__PerformTask_SendGoal_Request;

// Struct for a sequence of roomie_msgs__action__PerformTask_SendGoal_Request.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Request__Sequence
{
  roomie_msgs__action__PerformTask_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_SendGoal_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} roomie_msgs__action__PerformTask_SendGoal_Response;

// Struct for a sequence of roomie_msgs__action__PerformTask_SendGoal_Response.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Response__Sequence
{
  roomie_msgs__action__PerformTask_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_SendGoal_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  roomie_msgs__action__PerformTask_SendGoal_Event__request__MAX_SIZE = 1
};
// response
enum
{
  roomie_msgs__action__PerformTask_SendGoal_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Event
{
  service_msgs__msg__ServiceEventInfo info;
  roomie_msgs__action__PerformTask_SendGoal_Request__Sequence request;
  roomie_msgs__action__PerformTask_SendGoal_Response__Sequence response;
} roomie_msgs__action__PerformTask_SendGoal_Event;

// Struct for a sequence of roomie_msgs__action__PerformTask_SendGoal_Event.
typedef struct roomie_msgs__action__PerformTask_SendGoal_Event__Sequence
{
  roomie_msgs__action__PerformTask_SendGoal_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_SendGoal_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} roomie_msgs__action__PerformTask_GetResult_Request;

// Struct for a sequence of roomie_msgs__action__PerformTask_GetResult_Request.
typedef struct roomie_msgs__action__PerformTask_GetResult_Request__Sequence
{
  roomie_msgs__action__PerformTask_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_GetResult_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "roomie_msgs/action/detail/perform_task__struct.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_GetResult_Response
{
  int8_t status;
  roomie_msgs__action__PerformTask_Result result;
} roomie_msgs__action__PerformTask_GetResult_Response;

// Struct for a sequence of roomie_msgs__action__PerformTask_GetResult_Response.
typedef struct roomie_msgs__action__PerformTask_GetResult_Response__Sequence
{
  roomie_msgs__action__PerformTask_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_GetResult_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  roomie_msgs__action__PerformTask_GetResult_Event__request__MAX_SIZE = 1
};
// response
enum
{
  roomie_msgs__action__PerformTask_GetResult_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_GetResult_Event
{
  service_msgs__msg__ServiceEventInfo info;
  roomie_msgs__action__PerformTask_GetResult_Request__Sequence request;
  roomie_msgs__action__PerformTask_GetResult_Response__Sequence response;
} roomie_msgs__action__PerformTask_GetResult_Event;

// Struct for a sequence of roomie_msgs__action__PerformTask_GetResult_Event.
typedef struct roomie_msgs__action__PerformTask_GetResult_Event__Sequence
{
  roomie_msgs__action__PerformTask_GetResult_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_GetResult_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "roomie_msgs/action/detail/perform_task__struct.h"

/// Struct defined in action/PerformTask in the package roomie_msgs.
typedef struct roomie_msgs__action__PerformTask_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  roomie_msgs__action__PerformTask_Feedback feedback;
} roomie_msgs__action__PerformTask_FeedbackMessage;

// Struct for a sequence of roomie_msgs__action__PerformTask_FeedbackMessage.
typedef struct roomie_msgs__action__PerformTask_FeedbackMessage__Sequence
{
  roomie_msgs__action__PerformTask_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__action__PerformTask_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_H_
