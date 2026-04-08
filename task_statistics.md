# 任务统计分析

## 统计指标说明
- **avg_index**: 平均运行索引（每个task的index的算术平均值）
- **avg_score**: 平均得分（忽略nan和inf的有效分数的平均值）
- **std_score**: 得分标准差（样本标准差，用于衡量得分的波动性）

## 统计结果表

| task | avg_index | avg_score | std_score |
|------|-----------|-----------|-----------|
| change_point_detect_1 | 2.5000 | 0.1111 | 0.1571 |
| change_point_detect_2 | 2.0000 | 0.0000 | 0.0000 |
| change_point_detect_3 | 1.5000 | 0.0297 | 0.0420 |
| change_point_detect_4 | 2.0000 | 0.0612 | 0.0865 |
| ecg_data-extrapolation | 2.5000 | 0.1195 | 0.1450 |
| ecg_data-gaussian | 1.5000 | 0.0008 | 0.0006 |
| ecg_data-heartrate | 2.0000 | 56.6229 | 21.1134 |
| ecg_data-imputation | 2.0000 | 0.0207 | 0.0075 |
| ecg_data-motion | 2.0000 | 0.0075 | 0.0127 |
| ecg_data-powerline_1 | 2.0000 | 0.0000 | 0.0000 |
| ecg_data-powerline_2 | 2.0000 | 0.0000 | 0.0000 |
| gait-delay_detection | 2.0000 | 0.0004 | 0.0003 |
| gait-period_detection | 2.0000 | 0.1658 | 0.2473 |
| outlier_detect_1 | 1.5000 | 0.4990 | 0.6561 |
| outlier_detect_2 | 2.0000 | 0.6775 | 0.3859 |
| outlier_detect_3 | 2.0000 | 0.3833 | 0.3753 |
| outlier_detect_4 | 2.0000 | 0.2639 | 0.1203 |
| ppg-extrapolation | 2.0000 | 334.8053 | 578.8808 |
| ppg-imputation | 2.0000 | 1103.3283 | 1910.6384 |
| resampling | 2.0000 | 0.6719 | 1.0483 |
| speech-Siren | 2.0000 | 4.0646 | 3.2714 |
| speech-TelephoneRing1 | 2.0000 | -5.2888 | 19.1954 |
| speech-TelephoneRing2 | 2.0000 | 8.6045 | 1.4064 |
| speech-TelephoneRing3 | 2.0000 | 6.8092 | 3.0475 |
| speech-echo | 2.0000 | -19.9657 | 16.8774 |

## 主要发现

- **最高平均得分**: ppg-imputation (1103.3283)
- **最低平均得分**: speech-echo (-19.9657)
- **最稳定的任务（标准差最小）**: ecg_data-gaussian (0.0006)
- **波动最大的任务**: ppg-imputation (1910.6384)
- **数据点数**: 大多数任务有3个数据点，部分任务有2个数据点
