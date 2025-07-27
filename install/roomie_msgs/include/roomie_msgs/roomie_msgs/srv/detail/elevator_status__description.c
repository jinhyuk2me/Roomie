// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:srv/ElevatorStatus.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/srv/detail/elevator_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__ElevatorStatus__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x04, 0xe6, 0x1b, 0x9f, 0xec, 0xf8, 0x73, 0x16,
      0x4c, 0xfa, 0x14, 0xcb, 0xdb, 0x81, 0xf1, 0xbb,
      0x9d, 0x25, 0x99, 0x73, 0x5e, 0x41, 0xf8, 0xe1,
      0x93, 0x66, 0xd6, 0x86, 0xb2, 0xf3, 0xfc, 0x04,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__ElevatorStatus_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xb5, 0xd3, 0xd4, 0xe3, 0x5d, 0x33, 0xfb, 0xe8,
      0x5e, 0x37, 0xa3, 0x5a, 0xc4, 0x39, 0xe3, 0xc7,
      0x5d, 0x17, 0x28, 0x3d, 0xaf, 0xaa, 0x20, 0x6e,
      0xe7, 0xff, 0xc6, 0xad, 0xbb, 0x2f, 0xf5, 0x67,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__ElevatorStatus_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x3e, 0xb2, 0x89, 0xb5, 0xb1, 0xb5, 0xa8, 0xf5,
      0x5c, 0x32, 0x24, 0xc5, 0x7a, 0x58, 0x28, 0xad,
      0x15, 0x56, 0x1c, 0xa9, 0xab, 0x27, 0x16, 0x50,
      0xe0, 0x0f, 0x73, 0x6f, 0x59, 0x72, 0xbf, 0x90,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__ElevatorStatus_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x28, 0xaa, 0x75, 0x46, 0xcf, 0x8b, 0x95, 0xb8,
      0x4d, 0x81, 0xba, 0xe3, 0xc4, 0x7f, 0xe9, 0xb2,
      0x8a, 0x05, 0xa4, 0x3f, 0xfd, 0x6b, 0x6d, 0x7d,
      0x4f, 0xa6, 0x00, 0x53, 0xbe, 0x08, 0x70, 0x26,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char roomie_msgs__srv__ElevatorStatus__TYPE_NAME[] = "roomie_msgs/srv/ElevatorStatus";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char roomie_msgs__srv__ElevatorStatus_Event__TYPE_NAME[] = "roomie_msgs/srv/ElevatorStatus_Event";
static char roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME[] = "roomie_msgs/srv/ElevatorStatus_Request";
static char roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME[] = "roomie_msgs/srv/ElevatorStatus_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char roomie_msgs__srv__ElevatorStatus__FIELD_NAME__request_message[] = "request_message";
static char roomie_msgs__srv__ElevatorStatus__FIELD_NAME__response_message[] = "response_message";
static char roomie_msgs__srv__ElevatorStatus__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__ElevatorStatus__FIELDS[] = {
  {
    {roomie_msgs__srv__ElevatorStatus__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__ElevatorStatus_Event__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__ElevatorStatus__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Event__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__ElevatorStatus__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__ElevatorStatus__TYPE_NAME, 30, 30},
      {roomie_msgs__srv__ElevatorStatus__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__ElevatorStatus__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__ElevatorStatus_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__ElevatorStatus_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = roomie_msgs__srv__ElevatorStatus_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__ElevatorStatus_Request__FIELD_NAME__robot_id[] = "robot_id";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__ElevatorStatus_Request__FIELDS[] = {
  {
    {roomie_msgs__srv__ElevatorStatus_Request__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__ElevatorStatus_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
      {roomie_msgs__srv__ElevatorStatus_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__success[] = "success";
static char roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__direction[] = "direction";
static char roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__position[] = "position";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__ElevatorStatus_Response__FIELDS[] = {
  {
    {roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__success, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__direction, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Response__FIELD_NAME__position, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__ElevatorStatus_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
      {roomie_msgs__srv__ElevatorStatus_Response__FIELDS, 4, 4},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__info[] = "info";
static char roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__request[] = "request";
static char roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__ElevatorStatus_Event__FIELDS[] = {
  {
    {roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__ElevatorStatus_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__ElevatorStatus_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__ElevatorStatus_Event__TYPE_NAME, 36, 36},
      {roomie_msgs__srv__ElevatorStatus_Event__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__ElevatorStatus_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__ElevatorStatus_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__ElevatorStatus_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# ElevatorStatus.srv\n"
  "# Request\n"
  "int32 robot_id\n"
  "---\n"
  "# Response\n"
  "int32 robot_id\n"
  "bool success\n"
  "int32 direction\n"
  "int32 position\n"
  "\n"
  "# direction values:\n"
  "# 0: upward\n"
  "# 1: downward\n"
  "# position: \\xed\\x98\\x84\\xec\\x9e\\xac \\xec\\xb8\\xb5 ";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__ElevatorStatus__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__ElevatorStatus__TYPE_NAME, 30, 30},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 184, 184},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__ElevatorStatus_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__ElevatorStatus_Request__TYPE_NAME, 38, 38},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__ElevatorStatus_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__ElevatorStatus_Response__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__ElevatorStatus_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__ElevatorStatus_Event__TYPE_NAME, 36, 36},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__ElevatorStatus__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__ElevatorStatus__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__ElevatorStatus_Event__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__ElevatorStatus_Request__get_individual_type_description_source(NULL);
    sources[4] = *roomie_msgs__srv__ElevatorStatus_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__ElevatorStatus_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__ElevatorStatus_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__ElevatorStatus_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__ElevatorStatus_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__ElevatorStatus_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__ElevatorStatus_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__ElevatorStatus_Request__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__ElevatorStatus_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
