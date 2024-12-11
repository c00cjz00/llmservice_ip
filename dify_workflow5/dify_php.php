<?php
set_time_limit(600);

// Turn off deprecated warnings
error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);

// Optionally, you can turn off displaying errors (this can be done in php.ini as well)
ini_set('display_errors', 0);

require 'dify_php_lib.php'; // 假設這是您的程式碼檔案

// 初始化 WorkflowClient
$apiKey = 'app-4MDU7DKFkp4hHuKqMpOI7cqv';
#$apiKey = 'app-wFalyVLPBDEOouoRDr3vzD1H';
$base_url = 'https://trump.biobank.org.tw/v1/';
$userId = 'test_user'; // 用戶 ID
$workflowClient = new WorkflowClient($apiKey, $base_url);
$query="今天天氣很好為何會下雨";

// 運行工作流程
try {
    $inputs = [
        'query' => "the weatheris good",
    ];
    $responseMode = 'blocking'; // 使用阻塞模式

    // 調用運行工作流程的方法
    $response = $workflowClient->run($inputs, $responseMode, $userId);

    // 讀取和解析響應
    $bodyStream = $response->getBody();
    $fullResponse = '';

    while (!$bodyStream->eof()) {
        $fullResponse .= $bodyStream->read(1024); // 每次讀取 1024 字節
    }

    // 將完整響應轉換為 JSON
    $responseData = json_decode($fullResponse, true);

    // 檢查和輸出 "outputs": {"text": 部分
    if (isset($responseData['data']['outputs']['text'])) {
        echo $responseData['data']['outputs']['text'];
    } else {
        echo "Error: 'outputs' or 'text' key not found in the response.";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
