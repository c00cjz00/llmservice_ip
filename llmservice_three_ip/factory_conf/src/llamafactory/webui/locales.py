LOCALES = {
    "lang": {
        "en": {
            "label": "Lang"
        },
        "zh": {
            "label": "語言"
        }
    },
    "model_name": {
        "en": {
            "label": "Model name"
        },
        "zh": {
            "label": "模型名稱"
        }
    },
    "model_path": {
        "en": {
            "label": "Model path",
            "info": "Path to pretrained model or model identifier from Hugging Face."
        },
        "zh": {
            "label": "模型路徑",
            "info": "本地模型的檔案路徑或 Hugging Face 的模型識別符號。"
        }
    },
    "finetuning_type": {
        "en": {
            "label": "Finetuning method"
        },
        "zh": {
            "label": "微調方法"
        }
    },
    "adapter_path": {
        "en": {
            "label": "Adapter path"
        },
        "zh": {
            "label": "Adapter路徑"
        }
    },
    "refresh_btn": {
        "en": {
            "value": "Refresh adapters"
        },
        "zh": {
            "value": "重新整理Adapter"
        }
    },
    "advanced_tab": {
        "en": {
            "label": "Advanced configurations"
        },
        "zh": {
            "label": "高階設定"
        }
    },
    "quantization_bit": {
        "en": {
            "label": "Quantization bit",
            "info": "Enable 4/8-bit model quantization (QLoRA)."
        },
        "zh": {
            "label": "量化等級",
            "info": "啟用 4/8 位元模型量化（QLoRA）。"
        }
    },
    "template": {
        "en": {
            "label": "Prompt template",
            "info": "The template used in constructing prompts."
        },
        "zh": {
            "label": "提示模板",
            "info": "構建提示詞時使用的模板"
        }
    },
    "rope_scaling": {
        "en": {
            "label": "RoPE scaling"
        },
        "zh": {
            "label": "RoPE 插值方法"
        }
    },
    "booster": {
        "en": {
            "label": "Booster"
        },
        "zh": {
            "label": "加速方式"
        }
    },
    "visual_inputs": {
        "en": {
            "label": "Visual inputs"
        },
        "zh": {
            "label": "影象輸入"
        }
    },
    "training_stage": {
        "en": {
            "label": "Stage",
            "info": "The stage to perform in training."
        },
        "zh": {
            "label": "訓練階段",
            "info": "目前採用的訓練方式。"
        }
    },
    "dataset_dir": {
        "en": {
            "label": "Data dir",
            "info": "Path to the data directory."
        },
        "zh": {
            "label": "資料路徑",
            "info": "資料資料夾的路徑。"
        }
    },
    "dataset": {
        "en": {
            "label": "Dataset"
        },
        "zh": {
            "label": "資料集"
        }
    },
    "data_preview_btn": {
        "en": {
            "value": "Preview dataset"
        },
        "zh": {
            "value": "預覽資料集"
        }
    },
    "preview_count": {
        "en": {
            "label": "Count"
        },
        "zh": {
            "label": "數量"
        }
    },
    "page_index": {
        "en": {
            "label": "Page"
        },
        "zh": {
            "label": "頁數"
        }
    },
    "prev_btn": {
        "en": {
            "value": "Prev"
        },
        "zh": {
            "value": "上一頁"
        }
    },
    "next_btn": {
        "en": {
            "value": "Next"
        },
        "zh": {
            "value": "下一頁"
        }
    },
    "close_btn": {
        "en": {
            "value": "Close"
        },
        "zh": {
            "value": "關閉"
        }
    },
    "preview_samples": {
        "en": {
            "label": "Samples"
        },
        "zh": {
            "label": "樣例"
        }
    },
    "learning_rate": {
        "en": {
            "label": "Learning rate",
            "info": "Initial learning rate for AdamW."
        },
        "zh": {
            "label": "學習率",
            "info": "AdamW 最佳化器的初始學習率。"
        }
    },
    "num_train_epochs": {
        "en": {
            "label": "Epochs",
            "info": "Total number of training epochs to perform."
        },
        "zh": {
            "label": "訓練輪數",
            "info": "需要執行的訓練總輪數。"
        }
    },
    "max_grad_norm": {
        "en": {
            "label": "Maximum gradient norm",
            "info": "Norm for gradient clipping."
        },
        "zh": {
            "label": "最大梯度範數",
            "info": "用於梯度裁剪的範數。"
        }
    },
    "max_samples": {
        "en": {
            "label": "Max samples",
            "info": "Maximum samples per dataset."
        },
        "zh": {
            "label": "最大樣本數",
            "info": "每個資料集的最大樣本數。"
        }
    },
    "compute_type": {
        "en": {
            "label": "Compute type",
            "info": "Whether to use mixed precision training."
        },
        "zh": {
            "label": "計算型別",
            "info": "是否使用混合精度訓練。"
        }
    },
    "cutoff_len": {
        "en": {
            "label": "Cutoff length",
            "info": "Max tokens in input sequence."
        },
        "zh": {
            "label": "截斷長度",
            "info": "輸入序列分詞後的最大長度。"
        }
    },
    "batch_size": {
        "en": {
            "label": "Batch size",
            "info": "Number of samples processed on each GPU."
        },
        "zh": {
            "label": "批處理大小",
            "info": "每個 GPU 處理的樣本數量。"
        }
    },
    "gradient_accumulation_steps": {
        "en": {
            "label": "Gradient accumulation",
            "info": "Number of steps for gradient accumulation."
        },
        "zh": {
            "label": "梯度累積",
            "info": "梯度累積的步數。"
        }
    },
    "val_size": {
        "en": {
            "label": "Val size",
            "info": "Proportion of data in the dev set."
        },
        "zh": {
            "label": "驗證集比例",
            "info": "驗證集佔全部樣本的百分比。"
        }
    },
    "lr_scheduler_type": {
        "en": {
            "label": "LR scheduler",
            "info": "Name of the learning rate scheduler."
        },
        "zh": {
            "label": "學習率調節器",
            "info": "學習率排程器的名稱。"
        }
    },
    "extra_tab": {
        "en": {
            "label": "Extra configurations"
        },
        "zh": {
            "label": "其它引數設定"
        }
    },
    "logging_steps": {
        "en": {
            "label": "Logging steps",
            "info": "Number of steps between two logs."
        },
        "zh": {
            "label": "日誌間隔",
            "info": "每兩次日誌輸出間的更新步數。"
        }
    },
    "save_steps": {
        "en": {
            "label": "Save steps",
            "info": "Number of steps between two checkpoints."
        },
        "zh": {
            "label": "儲存間隔",
            "info": "每兩次斷點儲存間的更新步數。"
        }
    },
    "warmup_steps": {
        "en": {
            "label": "Warmup steps",
            "info": "Number of steps used for warmup."
        },
        "zh": {
            "label": "預熱步數",
            "info": "學習率預熱採用的步數。"
        }
    },
    "neftune_alpha": {
        "en": {
            "label": "NEFTune Alpha",
            "info": "Magnitude of noise adding to embedding vectors."
        },
        "zh": {
            "label": "NEFTune 噪聲引數",
            "info": "嵌入向量所新增的噪聲大小。"
        }
    },
    "optim": {
        "en": {
            "label": "Optimizer",
            "info": "The optimizer to use: adamw_torch, adamw_8bit or adafactor."
        },
        "zh": {
            "label": "最佳化器",
            "info": "使用的最佳化器：adamw_torch、adamw_8bit 或 adafactor。"
        }
    },
    "resize_vocab": {
        "en": {
            "label": "Resize token embeddings",
            "info": "Resize the tokenizer vocab and the embedding layers."
        },
        "zh": {
            "label": "更改詞表大小",
            "info": "更改分詞器詞表和嵌入層的大小。"
        }
    },
    "packing": {
        "en": {
            "label": "Pack sequences",
            "info": "Pack sequences into samples of fixed length."
        },
        "zh": {
            "label": "序列打包",
            "info": "將序列打包為等長樣本。"
        }
    },
    "upcast_layernorm": {
        "en": {
            "label": "Upcast LayerNorm",
            "info": "Upcast weights of layernorm in float32."
        },
        "zh": {
            "label": "縮放歸一化層",
            "info": "將歸一化層權重縮放至 32 位精度。"
        }
    },
    "use_llama_pro": {
        "en": {
            "label": "Enable LLaMA Pro",
            "info": "Make the parameters in the expanded blocks trainable."
        },
        "zh": {
            "label": "使用 LLaMA Pro",
            "info": "僅訓練塊擴充套件後的引數。"
        }
    },
    "shift_attn": {
        "en": {
            "label": "Enable S^2 Attention",
            "info": "Use shift short attention proposed by LongLoRA."
        },
        "zh": {
            "label": "使用 S^2 Attention",
            "info": "使用 LongLoRA 提出的 shift short attention。"
        }
    },
    "report_to": {
        "en": {
            "label": "Enable external logger",
            "info": "Use TensorBoard or wandb to log experiment."
        },
        "zh": {
            "label": "啟用外部記錄面板",
            "info": "使用 TensorBoard 或 wandb 記錄實驗。"
        }
    },
    "freeze_tab": {
        "en": {
            "label": "Freeze tuning configurations"
        },
        "zh": {
            "label": "部分引數微調設定"
        }
    },
    "num_layer_trainable": {
        "en": {
            "label": "Trainable layers",
            "info": "The number of trainable layers."
        },
        "zh": {
            "label": "可訓練層數",
            "info": "可訓練模型層的數量。"
        }
    },
    "name_module_trainable": {
        "en": {
            "label": "Trainable modules",
            "info": "The name of trainable modules. Use commas to separate multiple modules."
        },
        "zh": {
            "label": "可訓練模組",
            "info": "可訓練模組的名稱。使用英文逗號分隔多個名稱。"
        }
    },
    "lora_tab": {
        "en": {
            "label": "LoRA configurations"
        },
        "zh": {
            "label": "LoRA 引數設定"
        }
    },
    "lora_rank": {
        "en": {
            "label": "LoRA rank",
            "info": "The rank of LoRA matrices."
        },
        "zh": {
            "label": "LoRA 秩",
            "info": "LoRA 矩陣的秩大小。"
        }
    },
    "lora_alpha": {
        "en": {
            "label": "LoRA alpha",
            "info": "Lora scaling coefficient."
        },
        "zh": {
            "label": "LoRA 縮放係數",
            "info": "LoRA 縮放係數大小。"
        }
    },
    "lora_dropout": {
        "en": {
            "label": "LoRA dropout",
            "info": "Dropout ratio of LoRA weights."
        },
        "zh": {
            "label": "LoRA 隨機丟棄",
            "info": "LoRA 權重隨機丟棄的機率。"
        }
    },
    "loraplus_lr_ratio": {
        "en": {
            "label": "LoRA+ LR ratio",
            "info": "The LR ratio of the B matrices in LoRA."
        },
        "zh": {
            "label": "LoRA+ 學習率比例",
            "info": "LoRA+ 中 B 矩陣的學習率倍數。"
        }
    },
    "create_new_adapter": {
        "en": {
            "label": "Create new adapter",
            "info": "Create a new adapter with randomly initialized weight upon the existing one."
        },
        "zh": {
            "label": "新建Adapter",
            "info": "在現有的Adapter上建立一個隨機初始化後的新Adapter。"
        }
    },
    "use_rslora": {
        "en": {
            "label": "Use rslora",
            "info": "Use the rank stabilization scaling factor for LoRA layer."
        },
        "zh": {
            "label": "使用 rslora",
            "info": "對 LoRA 層使用秩穩定縮放方法。"
        }
    },
    "use_dora": {
        "en": {
            "label": "Use DoRA",
            "info": "Use weight-decomposed LoRA."
        },
        "zh": {
            "label": "使用 DoRA",
            "info": "使用權重分解的 LoRA。"
        }
    },
    "lora_target": {
        "en": {
            "label": "LoRA modules (optional)",
            "info": "Name(s) of modules to apply LoRA. Use commas to separate multiple modules."
        },
        "zh": {
            "label": "LoRA 作用模組（非必填）",
            "info": "應用 LoRA 的模組名稱。使用英文逗號分隔多個名稱。"
        }
    },
    "additional_target": {
        "en": {
            "label": "Additional modules (optional)",
            "info": "Name(s) of modules apart from LoRA layers to be set as trainable. Use commas to separate multiple modules."
        },
        "zh": {
            "label": "附加模組（非必填）",
            "info": "除 LoRA 層以外的可訓練模組名稱。使用英文逗號分隔多個名稱。"
        }
    },
    "rlhf_tab": {
        "en": {
            "label": "RLHF configurations"
        },
        "zh": {
            "label": "RLHF 引數設定"
        }
    },
    "dpo_beta": {
        "en": {
            "label": "DPO beta",
            "info": "Value of the beta parameter in the DPO loss."
        },
        "zh": {
            "label": "DPO beta 引數",
            "info": "DPO 損失函式中 beta 超引數大小。"
        }
    },
    "dpo_ftx": {
        "en": {
            "label": "DPO-ftx weight",
            "info": "The weight of SFT loss in the DPO-ftx."
        },
        "zh": {
            "label": "DPO-ftx 權重",
            "info": "DPO-ftx 中 SFT 損失的權重大小。"
        }
    },
    "orpo_beta": {
        "en": {
            "label": "ORPO beta",
            "info": "Value of the beta parameter in the ORPO loss."
        },
        "zh": {
            "label": "ORPO beta 引數",
            "info": "ORPO 損失函式中 beta 超引數大小。"
        }
    },
    "reward_model": {
        "en": {
            "label": "Reward model",
            "info": "Adapter of the reward model for PPO training."
        },
        "zh": {
            "label": "獎勵模型",
            "info": "PPO 訓練中獎勵模型的Adapter路徑。"
        }
    },
    "galore_tab": {
        "en": {
            "label": "GaLore configurations"
        },
        "zh": {
            "label": "GaLore 引數設定"
        }
    },
    "use_galore": {
        "en": {
            "label": "Use GaLore",
            "info": "Enable gradient low-Rank projection."
        },
        "zh": {
            "label": "使用 GaLore",
            "info": "使用梯度低秩投影。"
        }
    },
    "galore_rank": {
        "en": {
            "label": "GaLore rank",
            "info": "The rank of GaLore gradients."
        },
        "zh": {
            "label": "GaLore 秩",
            "info": "GaLore 梯度的秩大小。"
        }
    },
    "galore_update_interval": {
        "en": {
            "label": "Update interval",
            "info": "Number of steps to update the GaLore projection."
        },
        "zh": {
            "label": "更新間隔",
            "info": "相鄰兩次投影更新的步數。"
        }
    },
    "galore_scale": {
        "en": {
            "label": "GaLore scale",
            "info": "GaLore scaling coefficient."
        },
        "zh": {
            "label": "GaLore 縮放係數",
            "info": "GaLore 縮放係數大小。"
        }
    },
    "galore_target": {
        "en": {
            "label": "GaLore modules",
            "info": "Name(s) of modules to apply GaLore. Use commas to separate multiple modules."
        },
        "zh": {
            "label": "GaLore 作用模組",
            "info": "應用 GaLore 的模組名稱。使用英文逗號分隔多個名稱。"
        }
    },
    "badam_tab": {
        "en": {
            "label": "BAdam configurations"
        },
        "zh": {
            "label": "BAdam 引數設定"
        }
    },
    "use_badam": {
        "en": {
            "label": "Use BAdam",
            "info": "Enable the BAdam optimizer."
        },
        "zh": {
            "label": "使用 BAdam",
            "info": "使用 BAdam 最佳化器。"
        }
    },
    "badam_mode": {
        "en": {
            "label": "BAdam mode",
            "info": "Whether to use layer-wise or ratio-wise BAdam optimizer."
        },
        "zh": {
            "label": "BAdam 模式",
            "info": "使用 layer-wise 或 ratio-wise BAdam 最佳化器。"
        }
    },
    "badam_switch_mode": {
        "en": {
            "label": "Switch mode",
            "info": "The strategy of picking block to update for layer-wise BAdam."
        },
        "zh": {
            "label": "切換策略",
            "info": "Layer-wise BAdam 最佳化器的塊切換策略。"
        }
    },
    "badam_switch_interval": {
        "en": {
            "label": "Switch interval",
            "info": "Number of steps to update the block for layer-wise BAdam."
        },
        "zh": {
            "label": "切換頻率",
            "info": "Layer-wise BAdam 最佳化器的塊切換頻率。"
        }
    },
    "badam_update_ratio": {
        "en": {
            "label": "Update ratio",
            "info": "The ratio of the update for ratio-wise BAdam."
        },
        "zh": {
            "label": "Block 更新比例",
            "info": "Ratio-wise BAdam 最佳化器的更新比例。"
        }
    },
    "cmd_preview_btn": {
        "en": {
            "value": "Preview command"
        },
        "zh": {
            "value": "預覽命令"
        }
    },
    "arg_save_btn": {
        "en": {
            "value": "Save arguments"
        },
        "zh": {
            "value": "儲存訓練引數"
        }
    },
    "arg_load_btn": {
        "en": {
            "value": "Load arguments"
        },
        "zh": {
            "value": "載入訓練引數"
        }
    },
    "start_btn": {
        "en": {
            "value": "Start"
        },
        "zh": {
            "value": "開始"
        }
    },
    "stop_btn": {
        "en": {
            "value": "Abort"
        },
        "zh": {
            "value": "中斷"
        }
    },
    "output_dir": {
        "en": {
            "label": "Output dir",
            "info": "Directory for saving results."
        },
        "zh": {
            "label": "輸出目錄",
            "info": "儲存結果的路徑。"
        }
    },
    "config_path": {
        "en": {
            "label": "Config path",
            "info": "Path to config saving arguments."
        },
        "zh": {
            "label": "配置路徑",
            "info": "儲存訓練引數的配置檔案路徑。"
        }
    },
    "output_box": {
        "en": {
            "value": "Ready."
        },
        "zh": {
            "value": "準備就緒。"
        }
    },
    "loss_viewer": {
        "en": {
            "label": "Loss"
        },
        "zh": {
            "label": "損失"
        }
    },
    "predict": {
        "en": {
            "label": "Save predictions"
        },
        "zh": {
            "label": "儲存預測結果"
        }
    },
    "infer_backend": {
        "en": {
            "label": "Inference engine"
        },
        "zh": {
            "label": "推理引擎"
        }
    },
    "load_btn": {
        "en": {
            "value": "Load model"
        },
        "zh": {
            "value": "載入模型"
        }
    },
    "unload_btn": {
        "en": {
            "value": "Unload model"
        },
        "zh": {
            "value": "解除安裝模型"
        }
    },
    "info_box": {
        "en": {
            "value": "Model unloaded, please load a model first."
        },
        "zh": {
            "value": "模型未載入，請先載入模型。"
        }
    },
    "role": {
        "en": {
            "label": "Role"
        },
        "zh": {
            "label": "角色"
        }
    },
    "system": {
        "en": {
            "placeholder": "System prompt (optional)"
        },
        "zh": {
            "placeholder": "系統提示詞（非必填）"
        }
    },
    "tools": {
        "en": {
            "placeholder": "Tools (optional)"
        },
        "zh": {
            "placeholder": "工具列表（非必填）"
        }
    },
    "image": {
        "en": {
            "label": "Image (optional)"
        },
        "zh": {
            "label": "影象（非必填）"
        }
    },
    "query": {
        "en": {
            "placeholder": "Input..."
        },
        "zh": {
            "placeholder": "輸入..."
        }
    },
    "submit_btn": {
        "en": {
            "value": "Submit"
        },
        "zh": {
            "value": "提交"
        }
    },
    "max_length": {
        "en": {
            "label": "Maximum length"
        },
        "zh": {
            "label": "最大長度"
        }
    },
    "max_new_tokens": {
        "en": {
            "label": "Maximum new tokens"
        },
        "zh": {
            "label": "最大生成長度"
        }
    },
    "top_p": {
        "en": {
            "label": "Top-p"
        },
        "zh": {
            "label": "Top-p 取樣值"
        }
    },
    "temperature": {
        "en": {
            "label": "Temperature"
        },
        "zh": {
            "label": "溫度係數"
        }
    },
    "clear_btn": {
        "en": {
            "value": "Clear history"
        },
        "zh": {
            "value": "清空歷史"
        }
    },
    "export_size": {
        "en": {
            "label": "Max shard size (GB)",
            "info": "The maximum size for a model file."
        },
        "zh": {
            "label": "最大分塊大小（GB）",
            "info": "單個模型檔案的最大大小。"
        }
    },
    "export_quantization_bit": {
        "en": {
            "label": "Export quantization bit.",
            "info": "Quantizing the exported model."
        },
        "zh": {
            "label": "匯出量化等級",
            "info": "量化匯出模型。"
        }
    },
    "export_quantization_dataset": {
        "en": {
            "label": "Export quantization dataset",
            "info": "The calibration dataset used for quantization."
        },
        "zh": {
            "label": "匯出量化資料集",
            "info": "量化過程中使用的校準資料集。"
        }
    },
    "export_device": {
        "en": {
            "label": "Export device",
            "info": "Which device should be used to export model."
        },
        "zh": {
            "label": "匯出裝置",
            "info": "匯出模型使用的裝置型別。"
        }
    },
    "export_legacy_format": {
        "en": {
            "label": "Export legacy format",
            "info": "Do not use safetensors to save the model."
        },
        "zh": {
            "label": "匯出舊格式",
            "info": "不使用 safetensors 格式儲存模型。"
        }
    },
    "export_dir": {
        "en": {
            "label": "Export dir",
            "info": "Directory to save exported model."
        },
        "zh": {
            "label": "匯出目錄",
            "info": "儲存匯出模型的資料夾路徑。"
        }
    },
    "export_hub_model_id": {
        "en": {
            "label": "HF Hub ID (optional)",
            "info": "Repo ID for uploading model to Hugging Face hub."
        },
        "zh": {
            "label": "HF Hub ID（非必填）",
            "info": "用於將模型上傳至 Hugging Face Hub 的倉庫 ID。"
        }
    },
    "export_btn": {
        "en": {
            "value": "Export"
        },
        "zh": {
            "value": "開始匯出"
        }
    }
}


ALERTS = {
    "err_conflict": {
        "en": "A process is in running, please abort it first.",
        "zh": "任務已存在，請先中斷訓練。"
    },
    "err_exists": {
        "en": "You have loaded a model, please unload it first.",
        "zh": "模型已存在，請先解除安裝模型。"
    },
    "err_no_model": {
        "en": "Please select a model.",
        "zh": "請選擇模型。"
    },
    "err_no_path": {
        "en": "Model not found.",
        "zh": "模型未找到。"
    },
    "err_no_dataset": {
        "en": "Please choose a dataset.",
        "zh": "請選擇資料集。"
    },
    "err_no_adapter": {
        "en": "Please select an adapter.",
        "zh": "請選擇Adapter。"
    },
    "err_no_reward_model": {
        "en": "Please select a reward model.",
        "zh": "請選擇獎勵模型。"
    },
    "err_no_export_dir": {
        "en": "Please provide export dir.",
        "zh": "請填寫匯出目錄。"
    },
    "err_gptq_lora": {
        "en": "Please merge adapters before quantizing the model.",
        "zh": "量化模型前請先合併Adapter。"
    },
    "err_failed": {
        "en": "Failed.",
        "zh": "訓練出錯。"
    },
    "err_demo": {
        "en": "Training is unavailable in demo mode, duplicate the space to a private one first.",
        "zh": "展示模式不支援訓練，請先複製到私人空間。"
    },
    "err_device_count": {
        "en": "Multiple GPUs are not supported yet.",
        "zh": "尚不支援多 GPU 訓練。"
    },
    "err_tool_name": {
        "en": "Tool name not found.",
        "zh": "工具名稱未找到。"
    },
    "err_json_schema": {
        "en": "Invalid JSON schema.",
        "zh": "Json 格式錯誤。"
    },
    "err_config_not_found": {
        "en": "Config file is not found.",
        "zh": "未找到配置檔案。"
    },
    "warn_no_cuda": {
        "en": "CUDA environment was not detected.",
        "zh": "未檢測到 CUDA 環境。"
    },
    "info_aborting": {
        "en": "Aborted, wait for terminating...",
        "zh": "訓練中斷，正在等待程序結束……"
    },
    "info_aborted": {
        "en": "Ready.",
        "zh": "準備就緒。"
    },
    "info_finished": {
        "en": "Finished.",
        "zh": "訓練完畢。"
    },
    "info_config_saved": {
        "en": "Arguments have been saved at: ",
        "zh": "訓練引數已儲存至："
    },
    "info_config_loaded": {
        "en": "Arguments have been restored.",
        "zh": "訓練引數已載入。"
    },
    "info_loading": {
        "en": "Loading model...",
        "zh": "載入中……"
    },
    "info_unloading": {
        "en": "Unloading model...",
        "zh": "解除安裝中……"
    },
    "info_loaded": {
        "en": "Model loaded, now you can chat with your model!",
        "zh": "模型已載入，可以開始聊天了！"
    },
    "info_unloaded": {
        "en": "Model unloaded.",
        "zh": "模型已解除安裝。"
    },
    "info_exporting": {
        "en": "Exporting model...",
        "zh": "正在匯出模型……"
    },
    "info_exported": {
        "en": "Model exported.",
        "zh": "模型匯出完成。"
    }
}
