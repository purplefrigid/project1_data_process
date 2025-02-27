import numpy as np  
from sklearn.ensemble import IsolationForest  
from sklearn.decomposition import PCA  
from sklearn.cluster import DBSCAN  
import pandas as pd  

Project_folder = "D:\\keti\\zjh\\"   
path = Project_folder + "modified_file1.xlsx"
                                 # 设置空列表，用于存放样本的index
df = pd.read_excel(path)
# Step 1: 数据加载与预处理  
# 假设 data 是一个 (1000, 100) 的 NumPy 数组  
# data = np.random.rand(1000, 100)  # 示例数据 
data = np.array(df.iloc[:, 17:115],dtype=np.float32)  
data_normalized = (data - np.min(data, axis=1, keepdims=True)) / (np.max(data, axis=1, keepdims=True) - np.min(data, axis=1, keepdims=True))  

# Step 2: 初步异常检测  
# 使用孤立森林检测异常  
isolation_forest = IsolationForest(contamination=0.05, random_state=42)  
anomaly_scores = isolation_forest.fit_predict(data_normalized)  

# 找出初步异常数据  
anomalies = np.where(anomaly_scores == -1)[0]  
print(f"初步检测到的异常数据索引: {anomalies}")  

# Step 3: 主动学习策略  
# 使用 PCA 降维以便可视化和进一步分析  
pca = PCA(n_components=2)  
data_pca = pca.fit_transform(data_normalized)  

# 使用 DBSCAN 聚类，进一步筛选异常点  
dbscan = DBSCAN(eps=0.5, min_samples=5)  
clusters = dbscan.fit_predict(data_pca)  

# 找出噪声点（DBSCAN 中的 -1 类）  
noise_points = np.where(clusters == -1)[0]  
print(f"DBSCAN 检测到的噪声点索引: {noise_points}")  

# Step 4: 人工验证与迭代  
# 将孤立森林和 DBSCAN 的结果结合，选择需要进一步分析的数据  
potential_errors = set(anomalies).union(set(noise_points))  
print(f"需要进一步分析的数据索引: {potential_errors}")
a=list(potential_errors)
for i in a:
    print(data[i][0])

output_file = "output.xlsx"  # 输出文件名  
df_cleaned = df.drop(index=a)  

# 将结果保存到新的 Excel 文件  
df_cleaned.to_excel(output_file, index=False)  

print(f"处理完成，剔除后的数据已保存到 {output_file}")