// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:srv/SpaceAvailability.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/srv/detail/space_availability__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__SpaceAvailability__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x07, 0xb5, 0x74, 0xfe, 0x06, 0xce, 0xd6, 0xaa,
      0x71, 0x4e, 0xda, 0xf1, 0xbe, 0xaf, 0x2e, 0x0d,
      0xbd, 0xfa, 0x1f, 0x06, 0xd3, 0x53, 0x29, 0x0a,
      0xcb, 0x9d, 0x3d, 0xc1, 0x72, 0xc4, 0x82, 0xff,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__SpaceAvailability_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x7e, 0x64, 0x66, 0x6f, 0x8e, 0x8e, 0x69, 0x57,
      0x72, 0x77, 0xb0, 0xba, 0x17, 0xfd, 0x28, 0xab,
      0xc6, 0x2f, 0x77, 0xe5, 0x4b, 0x0c, 0x3d, 0xf3,
      0xf5, 0x37, 0xc8, 0x84, 0x1c, 0x7a, 0x58, 0x92,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__SpaceAvailability_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf7, 0x8a, 0x69, 0xbf, 0xd5, 0x83, 0x5c, 0x92,
      0x9a, 0x41, 0x0a, 0xa7, 0xba, 0x8c, 0x06, 0x20,
      0x9e, 0x3f, 0xcf, 0x82, 0xa6, 0x99, 0x23, 0x20,
      0xa6, 0x46, 0x3c, 0x8f, 0x4b, 0xa8, 0x8f, 0x62,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__SpaceAvailability_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x3a, 0x9b, 0xe8, 0xc0, 0xf0, 0x69, 0xda, 0xb1,
      0x7b, 0x52, 0xf4, 0x8f, 0xfc, 0xa0, 0x18, 0xd0,
      0xa0, 0x4c, 0xae, 0x6e, 0x07, 0xe7, 0xb7, 0xd7,
      0x23, 0xd2, 0x5c, 0xd6, 0xf2, 0x0f, 0xf5, 0x6e,
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

static char roomie_msgs__srv__SpaceAvailability__TYPE_NAME[] = "roomie_msgs/srv/SpaceAvailability";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char roomie_msgs__srv__SpaceAvailability_Event__TYPE_NAME[] = "roomie_msgs/srv/SpaceAvailability_Event";
static char roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME[] = "roomie_msgs/srv/SpaceAvailability_Request";
static char roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME[] = "roomie_msgs/srv/SpaceAvailability_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char roomie_msgs__srv__SpaceAvailability__FIELD_NAME__request_message[] = "request_message";
static char roomie_msgs__srv__SpaceAvailability__FIELD_NAME__response_message[] = "response_message";
static char roomie_msgs__srv__SpaceAvailability__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__SpaceAvailability__FIELDS[] = {
  {
    {roomie_msgs__srv__SpaceAvailability__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__SpaceAvailability_Event__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__SpaceAvailability__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Event__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__SpaceAvailability__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__SpaceAvailability__TYPE_NAME, 33, 33},
      {roomie_msgs__srv__SpaceAvailability__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__SpaceAvailability__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__SpaceAvailability_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__SpaceAvailability_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = roomie_msgs__srv__SpaceAvailability_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__SpaceAvailability_Request__FIELD_NAME__robot_id[] = "robot_id";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__SpaceAvailability_Request__FIELDS[] = {
  {
    {roomie_msgs__srv__SpaceAvailability_Request__FIELD_NAME__robot_id, 8, 8},
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
roomie_msgs__srv__SpaceAvailability_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
      {roomie_msgs__srv__SpaceAvailability_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__success[] = "success";
static char roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__space_availability[] = "space_availability";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__SpaceAvailability_Response__FIELDS[] = {
  {
    {roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__success, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Response__FIELD_NAME__space_availability, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__SpaceAvailability_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
      {roomie_msgs__srv__SpaceAvailability_Response__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__info[] = "info";
static char roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__request[] = "request";
static char roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__SpaceAvailability_Event__FIELDS[] = {
  {
    {roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__SpaceAvailability_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__SpaceAvailability_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__SpaceAvailability_Event__TYPE_NAME, 39, 39},
      {roomie_msgs__srv__SpaceAvailability_Event__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__SpaceAvailability_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__SpaceAvailability_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__SpaceAvailability_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# SpaceAvailability.srv\n"
  "# Request\n"
  "int32 robot_id\n"
  "---\n"
  "# Response\n"
  "int32 robot_id\n"
  "bool success\n"
  "bool space_availability ";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__SpaceAvailability__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__SpaceAvailability__TYPE_NAME, 33, 33},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 116, 116},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__SpaceAvailability_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__SpaceAvailability_Request__TYPE_NAME, 41, 41},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__SpaceAvailability_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__SpaceAvailability_Response__TYPE_NAME, 42, 42},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__SpaceAvailability_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__SpaceAvailability_Event__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__SpaceAvailability__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__SpaceAvailability__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__SpaceAvailability_Event__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__SpaceAvailability_Request__get_individual_type_description_source(NULL);
    sources[4] = *roomie_msgs__srv__SpaceAvailability_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__SpaceAvailability_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__SpaceAvailability_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__SpaceAvailability_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__SpaceAvailability_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__SpaceAvailability_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__SpaceAvailability_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__SpaceAvailability_Request__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__SpaceAvailability_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
