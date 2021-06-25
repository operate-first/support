---
name: "User support: Kafka User/Topic request"
about: "Template for users to request Kafka Topics and User credentials/certs."
title: ""
labels: user-support
assignees: ""
---

## Questionnaire

### Kafka Topic

1. **Topic names**: TOPIC_NAME
   <!--
   A list of kafka topic names to be requested.
   -->

2. **Topic partitions**: 3
   <!--
   Number of topic partitions.

   Default: 3
   -->


3. **Topic replicas**: 2
   <!--
   Number of topic replicas.

   Default: 2
   -->


4. **Topic retention period**: 6 hours
   <!--
   Duration for which messages in the topic will be stored for.

   Default: 6 hours (21600000ms)
   -->


5. **Topic Configuration**: None
   <!--
   Other Kafka Topic configuration flags, example: "max.message.bytes: 10000000".

   Default: None
   -->

### Kafka Users

1. **User names**: USER_NAME
   <!--
   A list of kafka user names to be requested.
   -->

2. **Topic access**: TOPIC_NAMES
   <!--
   List of topics this user should have access to.

   Default: Above requested topics
   -->


3. **Consumer group ids**: GROUP_IDS
   <!--
   List of group ids used by clients.
   Please read how consumer groups work [here](https://www.tutorialspoint.com/apache_kafka/apache_kafka_consumer_group_example.htm)
   before submitting your request.
   You need at least one group id to be able to consume from requested topics.

   Default: Same as topic names
   -->


4. **Your GPG key or contact**:
   <!--
   Please specify, how we can reach out to you securely so we
   can share your kafka user credentials and access details.
   Providing us with your GPG key is preferred. Example:

   `0508677DD04952D06A943D5B4DC4116D360E3276` available from keys.gnupg.net
   -->

---

If you don't want to wait for the maintainers to notice this issue, you can do the changes yourself. Please follow the [Add Kafka Topics](https://github.com/operate-first/apps/blob/master/docs/odh/kafka/README.md#adding-kafka-topics) guide.
