// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:srv/CheckItemLoaded.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/srv/detail/check_item_loaded__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__CheckItemLoaded__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x43, 0x74, 0x18, 0xc5, 0xcc, 0x72, 0x74, 0x17,
      0x05, 0x42, 0xf9, 0xbe, 0xcd, 0x87, 0x57, 0xf1,
      0x57, 0x7d, 0xb4, 0x63, 0xd5, 0x2e, 0x02, 0xf2,
      0xc6, 0x1f, 0xb8, 0xff, 0xf3, 0x95, 0xf9, 0x43,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__CheckItemLoaded_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xd6, 0x3e, 0xad, 0x51, 0x02, 0xd4, 0x51, 0x14,
      0x45, 0xaa, 0x70, 0x37, 0xe8, 0xa5, 0x30, 0xe2,
      0x91, 0x6e, 0xa5, 0x73, 0x84, 0xf9, 0x96, 0x43,
      0xf0, 0x77, 0x1b, 0xed, 0xbd, 0x1e, 0xd0, 0x9f,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__CheckItemLoaded_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x3f, 0xaa, 0x63, 0x34, 0x0e, 0x95, 0x0a, 0x12,
      0x05, 0xd7, 0xae, 0x62, 0xd0, 0x79, 0xe2, 0xff,
      0xdf, 0x40, 0xf3, 0xe0, 0x94, 0x92, 0x6f, 0x66,
      0xf9, 0x26, 0x15, 0xd2, 0x58, 0xf2, 0xc5, 0x88,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__srv__CheckItemLoaded_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x66, 0xad, 0x7f, 0x97, 0x77, 0x4a, 0x74, 0x93,
      0x29, 0x36, 0x04, 0xc7, 0x2b, 0x2a, 0xad, 0x06,
      0x49, 0x3b, 0xfa, 0xe7, 0x63, 0x84, 0x9d, 0x5e,
      0xb2, 0x8a, 0x77, 0xbb, 0xdd, 0x11, 0x55, 0x74,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

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

static char roomie_msgs__srv__CheckItemLoaded__TYPE_NAME[] = "roomie_msgs/srv/CheckItemLoaded";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char roomie_msgs__srv__CheckItemLoaded_Event__TYPE_NAME[] = "roomie_msgs/srv/CheckItemLoaded_Event";
static char roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME[] = "roomie_msgs/srv/CheckItemLoaded_Request";
static char roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME[] = "roomie_msgs/srv/CheckItemLoaded_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__request_message[] = "request_message";
static char roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__response_message[] = "response_message";
static char roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__CheckItemLoaded__FIELDS[] = {
  {
    {roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {roomie_msgs__srv__CheckItemLoaded_Event__TYPE_NAME, 37, 37},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__CheckItemLoaded__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Event__TYPE_NAME, 37, 37},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__CheckItemLoaded__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__CheckItemLoaded__TYPE_NAME, 31, 31},
      {roomie_msgs__srv__CheckItemLoaded__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__CheckItemLoaded__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__CheckItemLoaded_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__CheckItemLoaded_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = roomie_msgs__srv__CheckItemLoaded_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__CheckItemLoaded_Request__FIELD_NAME__robot_id[] = "robot_id";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__CheckItemLoaded_Request__FIELDS[] = {
  {
    {roomie_msgs__srv__CheckItemLoaded_Request__FIELD_NAME__robot_id, 8, 8},
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
roomie_msgs__srv__CheckItemLoaded_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
      {roomie_msgs__srv__CheckItemLoaded_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__CheckItemLoaded_Response__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__srv__CheckItemLoaded_Response__FIELD_NAME__item_loaded[] = "item_loaded";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__CheckItemLoaded_Response__FIELDS[] = {
  {
    {roomie_msgs__srv__CheckItemLoaded_Response__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Response__FIELD_NAME__item_loaded, 11, 11},
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
roomie_msgs__srv__CheckItemLoaded_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
      {roomie_msgs__srv__CheckItemLoaded_Response__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__info[] = "info";
static char roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__request[] = "request";
static char roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field roomie_msgs__srv__CheckItemLoaded_Event__FIELDS[] = {
  {
    {roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__srv__CheckItemLoaded_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__srv__CheckItemLoaded_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__srv__CheckItemLoaded_Event__TYPE_NAME, 37, 37},
      {roomie_msgs__srv__CheckItemLoaded_Event__FIELDS, 3, 3},
    },
    {roomie_msgs__srv__CheckItemLoaded_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = roomie_msgs__srv__CheckItemLoaded_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = roomie_msgs__srv__CheckItemLoaded_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# CheckItemLoaded.srv\n"
  "# Request\n"
  "int32 robot_id\n"
  "---\n"
  "# Response\n"
  "int32 robot_id\n"
  "bool item_loaded\n"
  "\n"
  "# item_loaded values:\n"
  "# true: \\xeb\\xac\\xbc\\xed\\x92\\x88\\xec\\x9d\\xb4 \\xea\\xb0\\x90\\xec\\xa7\\x80\\xeb\\x90\\x9c \\xec\\x83\\x81\\xed\\x83\\x9c\n"
  "# false: \\xec\\x97\\x86\\xeb\\x8a\\x94 \\xec\\x83\\x81\\xed\\x83\\x9c ";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__CheckItemLoaded__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__CheckItemLoaded__TYPE_NAME, 31, 31},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 151, 151},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__CheckItemLoaded_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__CheckItemLoaded_Request__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__CheckItemLoaded_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__CheckItemLoaded_Response__TYPE_NAME, 40, 40},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__srv__CheckItemLoaded_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__srv__CheckItemLoaded_Event__TYPE_NAME, 37, 37},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__CheckItemLoaded__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__CheckItemLoaded__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__CheckItemLoaded_Event__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__CheckItemLoaded_Request__get_individual_type_description_source(NULL);
    sources[4] = *roomie_msgs__srv__CheckItemLoaded_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__CheckItemLoaded_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__CheckItemLoaded_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__CheckItemLoaded_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__CheckItemLoaded_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__srv__CheckItemLoaded_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__srv__CheckItemLoaded_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *roomie_msgs__srv__CheckItemLoaded_Request__get_individual_type_description_source(NULL);
    sources[3] = *roomie_msgs__srv__CheckItemLoaded_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
