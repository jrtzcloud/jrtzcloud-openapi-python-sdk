├── blten
│   ├── __init__.py
│   └── v20191120
│       ├── blten_client.py
│       ├── __init__.py
│       ├── models.py
├── common
│   ├── abstract_client.py
│   ├── abstract_model.py
│   ├── credential.py
│   ├── exception
│   │   ├── __init__.py
│   │   ├── jrtzcloud_sdk_exception.py
│   ├── http
│   │   ├── __init__.py
│   │   └── request.py
│   ├── __init__.py
│   ├── profile
│   │   ├── client_profile.py
│   │   ├── http_profile.py
│   │   ├── __init__.py
│   └── sign.py
├── data_api            # 数据API接口类
│   ├── __init__.py
│   └── v20191119
│       ├── ana_rank_est_idu.py     # 天眼分析师预测排名数据获取接口
│       ├── ana_rank_grd.py         # 天眼分析师评级排名数据获取接口
│       ├── data_api_client.py
│       ├── est_bsc.py              # 盈利预测数据获取接口
│       ├── grd_bsc.py              # 投资评级数据获取接口
│       ├── idu_cls_ref.py          # 行业分类参数数据获取接口
│       ├── ind_frcst_anaem.py      # 分析师动能数据获取接口
│       ├── ind_frcst_hist.py       # 一致预期历史数据获取接口
│       ├── ind_frcst_iduem.py      # 分析师行业动能数据获取接口
│       ├── ind_frcst_tianyan.py    # 天眼预期统计数据获取接口
│       ├── ind_rank_eq_idu.py      # 公司盈利质量数据获取接口
│       ├── ind_rank_pm.py          # 价格动能模型数据获取接口
│       ├── ind_rank_rv_idu.py      # 相对估值模型数据获取接口
│       ├── __init__.py
│       ├── models.py
│       ├── res_org_rank.py         # 研究机构整体实力得分数据获取接口
│       └── res_org_ref.py          # 研究机构接口参数数据获取接口
├── examples                        # 接口调用示例
│   ├── blten
│   │   └── v20191121
│   │       └── demo.py
│   └── data_api                    # 数据API接口调用示例
│       ├── __init__.py
│       └── v20191119
│           ├── demo_ana_rank_est_idu.py    # 天眼分析师预测排名数据接口调用示例
│           ├── demo_ana_rank_grd.py        # 天眼分析师评级排名数据接口调用示例
│           ├── demo_est_bsc.py             # 盈利预测数据接口调用示例
│           ├── demo_grd_bsc.py             # 投资评级数据接口调用示例
│           ├── demo_idu_cls_ref.py         # 行业分类参数数据接口调用示例
│           ├── demo_ind_frcst_anaem.py     # 分析师动能数据接口调用示例
│           ├── demo_ind_frcst_hist.py      # 一致预期历史数据接口调用示例
│           ├── demo_ind_frcst_iduem.py     # 分析师行业动能数据接口调用示例
│           ├── demo_ind_frcst_tianyan.py   # 天眼预期统计数据接口调用示例
│           ├── demo_ind_rank_eq_idu.py     # 公司盈利质量数据接口调用示例
│           ├── demo_ind_rank_pm.py         # 价格动能模型数据接口调用示例
│           ├── demo_ind_rank_rv_idu.py     # 相对估值模型数据接口调用示例
│           ├── demo_res_org_rank.py        # 研究机构整体实力得分数据接口调用示例
│           ├── demo_res_org_ref.py         # 研究机构接口参数数据接口调用示例
│           └── __init__.py
