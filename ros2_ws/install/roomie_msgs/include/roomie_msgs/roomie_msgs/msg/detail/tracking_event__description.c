// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:msg/TrackingEvent.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/msg/detail/tracking_event__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__TrackingEvent__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x59, 0x4a, 0x0e, 0x1c, 0x6a, 0x4a, 0x98, 0x18,
      0x0e, 0xfb, 0x90, 0xc0, 0xfd, 0xad, 0xc0, 0xf4,
      0x6e, 0x6c, 0xa7, 0xf3, 0x83, 0x7c, 0xc2, 0x51,
      0xf8, 0xf6, 0x6b, 0x9b, 0x66, 0x8e, 0x47, 0x3d,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
#endif

static char roomie_msgs__msg__TrackingEvent__TYPE_NAME[] = "roomie_msgs/msg/TrackingEvent";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char roomie_msgs__msg__TrackingEvent__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__msg__TrackingEvent__FIELD_NAME__tracking_event_id[] = "tracking_event_id";
static char roomie_msgs__msg__TrackingEvent__FIELD_NAME__task_id[] = "task_id";
static char roomie_msgs__msg__TrackingEvent__FIELD_NAME__timestamp[] = "timestamp";

static rosidl_runtime_c__type_description__Field roomie_msgs__msg__TrackingEvent__FIELDS[] = {
  {
    {roomie_msgs__msg__TrackingEvent__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__TrackingEvent__FIELD_NAME__tracking_event_id, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__TrackingEvent__FIELD_NAME__task_id, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__TrackingEvent__FIELD_NAME__timestamp, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__msg__TrackingEvent__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__TrackingEvent__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__msg__TrackingEvent__TYPE_NAME, 29, 29},
      {roomie_msgs__msg__TrackingEvent__FIELDS, 4, 4},
    },
    {roomie_msgs__msg__TrackingEvent__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# TrackingEvent.msg\n"
  "int32 robot_id\n"
  "int32 tracking_event_id\n"
  "int32 task_id\n"
  "builtin_interfaces/Time timestamp\n"
  "\n"
  "# tracking_event_id values:\n"
  "# 0: slow_down\n"
  "# 1: maintain\n"
  "# 2: lost\n"
  "# 3: resume ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__TrackingEvent__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__msg__TrackingEvent__TYPE_NAME, 29, 29},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 187, 187},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__TrackingEvent__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__msg__TrackingEvent__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
