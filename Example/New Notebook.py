# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW temp_vw_sumit(id, name, value) AS VALUES
# MAGIC (1, "A", 1.0),
# MAGIC (2, "B", 2.1)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM temp_vw_sumit

# COMMAND ----------

display(spark.sql("SELECT * FROM temp_vw_sumit"))
