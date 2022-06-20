# Databricks notebook source
# MAGIC %md
# MAGIC # Magic Commands
# MAGIC * %md komutu yorum olarak kaydediyor 
# MAGIC * %fs file system komutu
# MAGIC * %sh shell komutu

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/databricks-datasets/

# COMMAND ----------

# MAGIC %fs
# MAGIC ls 
# MAGIC dbfs:/databricks-datasets/COVID/

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/databricks-datasets/COVID/USAFacts/

# COMMAND ----------

# MAGIC %fs
# MAGIC head dbfs:/databricks-datasets/COVID/USAFacts/covid_deaths_usafacts.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC ps

# COMMAND ----------

