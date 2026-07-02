#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import re


# In[27]:


#Read in control starting population for validation

df = pd.read_excel("Synthetic_Control_Validation_Data.xlsx")


# In[28]:


#Verify data

df.head()


# In[29]:


print(f"{df} Record Count: {len(df)}")


# In[48]:


print(df["MESSAGE_TEXT"])


# In[49]:


# Extract audit types

message_text = df["MESSAGE_TEXT"].iloc[0]

audit_types = re.findall(r'auditType=([^,\s}]+)', message_text)

print(audit_types)


# In[38]:


# Extract auditors

auditors = re.findall(r'auditBy=([^,\s}]+)', message_text)

print(auditors)


# In[53]:


audit_df = pd.DataFrame({
    "maker": audit_types,
    "checker": auditors
})

print(audit_df)


# In[57]:


# Validation Rule 1
df["maker_checker_test"] = np.where(
    df["MAKER_ID"] == df["CHECKER_ID"],
    "FAIL",
    "PASS"
)


# In[68]:


# Validation Rule 2
df["date_sequence_test"] = np.where(
    df["BEFORE_ACTION_DATE"].dt.date == df["AFTER_ACTION_DATE"].dt.date,
    "PASS",
    "FAIL"
)


# In[69]:


# Final Output
print(
    df[
        [
            "TRANSACTION_REFERENCE_NO",
            "MAKER_ID",
            "CHECKER_ID",
            "maker_checker_test",
            "BEFORE_ACTION_DATE",
            "AFTER_ACTION_DATE",
            "date_sequence_test"
        ]
    ]
)


# In[ ]:




