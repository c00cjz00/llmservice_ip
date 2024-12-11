<?php
set_time_limit(600);
// Turn off deprecated warnings
error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
// Optionally, you can turn off displaying errors (this can be done in php.ini as well)
ini_set('display_errors', 0);
require 'dify_class.php'; // 假設這是您的程式碼檔案
// 初始化 WorkflowClient
$apiKey = 'app-';
$base_url = 'https://trump.biobank.org.tw/v1/';
$userId = 'test_user'; // 用戶 ID
$workflowClient = new WorkflowClient($apiKey, $base_url);

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize input data
    $office_document = htmlspecialchars(trim($_POST['office_document']));
    $title = htmlspecialchars(trim($_POST['title']));
    $content = htmlspecialchars(trim($_POST['content']));
    $a01 = htmlspecialchars(trim($_POST['a01']));
    $a02 = htmlspecialchars(trim($_POST['a02']));
    $a03 = htmlspecialchars(trim($_POST['a03']));
    $a04 = htmlspecialchars(trim($_POST['a04']));
    $a05 = htmlspecialchars(trim($_POST['a05']));
    $a06 = htmlspecialchars(trim($_POST['a06']));
    $a07 = htmlspecialchars(trim($_POST['a07']));
    $a08 = htmlspecialchars(trim($_POST['a08']));
    $a09 = htmlspecialchars(trim($_POST['a09']));
    $a10 = htmlspecialchars(trim($_POST['a10']));
    $a11 = htmlspecialchars(trim($_POST['a11']));
    $a12 = htmlspecialchars(trim($_POST['a12']));
    $a13 = htmlspecialchars(trim($_POST['a13']));
    $a14 = htmlspecialchars(trim($_POST['a14']));
    $a15 = htmlspecialchars(trim($_POST['a15']));
}else{
	$title="";
	$content="";
	$a01="";
	$a02="";
	$a03="";
	$a04="";
	$a05="";
	$a06="";
	$a07="";
	$a08="";
	$a09="";
	$a10="";
	$a11="";
	$a12="";
	$a13="";
	$a14="";
	$a15="";
}	
	
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>國家科學及技術委員會 生成式AI服務系統</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>

         /* 清除頁面默認間距 */
        body {
            margin: 0;
        }

        /* 頂部橫幅樣式 */
        .top-banner {
            #background-color: #ffc107; /* Bootstrap 的黃色變數 */
            background-color: #563D7C; /* Bootstrap 的黃色變數 */
            color: #F8F7F9; /* 黑色文字 */
            text-align: center;
            padding: 5px 10px;
            font-size: 14px;
            position: fixed; /* 固定在頁面頂部 */
            top: 0;
            width: 100%; /* 寬度 100% */
            z-index: 1030; /* 保證橫幅在最上層 */
        }

        /* 紫色 Navbar 樣式 */
        .navbar-purple {
            #background-color: #6f42c1; /* Bootstrap 的紫色變數 */
            background-color: #7952B3; /* Bootstrap 的紫色變數 */
            margin-top: 30px; /* 與橫幅無縫銜接 */
        }
        .navbar-purple .navbar-brand,
        .navbar-purple .nav-link {
            color: white;
        }
        .navbar-purple .nav-link:hover {
            color: #d8b9f8; /* 添加一個較淺的紫色作為 hover 效果 */
        }
		
	
        /* Textarea container width set to 70% */
        .textarea-container {
            width: 80%; /* Set container width to 70% */
            margin: 0 auto; /* Center the container */
        }

        /* Textarea width fills the container */
        .textarea2 {
            font-family: monospace;
            font-size: 0.7rem !important; /* Set font-size to 0.8rem and force it with !important */
            width: 100%; /* Make textarea fill 100% of its container */
            height: calc(1.5em * 20 + 2rem + 2px); /* 20 lines height with padding and border */
            display: block;
        }

        /* Set the form control elements to be 50% width and center them */
        form {
            width: 80%;
            margin: 0 auto; /* Center the form */
        }

        /* Initially hide fields */
        #titleField, #contentField, #a01Field, #a02Field, #a03Field, #a04Field, #a05Field, #a06Field, #a07Field, #a08Field, #a09Field, #a10Field, #a11Field, #a12Field, #a13Field, #a14Field, #a15Field {
            display: none;
        }
    </style>
</head>
<body>
	<!-- 頂部橫幅 -->
    <div class="top-banner">
		國家科學及技術委員會 生成式AI服務系統
    </div>

    <!-- 紫色 Navbar -->
    <nav class="navbar navbar-expand-lg navbar-purple">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">GENAI@NCHC</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">公文撰寫</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">新聞稿撰寫</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">立法院問答</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">民眾陳情</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Podcast製作</a>
                    </li>					
                </ul>
            </div>
        </div>
    </nav>
	<br>
    <h3 class="mb-4 text-center"><b>公文撰寫</b></h3>

    <!-- Form Section -->
    <form method="POST" action="" onsubmit="showLoadingModal()">
        <!-- office_document selection -->
        <div class="mb-3">
            <label for="office_document" class="form-label">公文類別</label>
            <select class="form-select" id="office_document" name="office_document" required onchange="toggleFields()">
                <option value="">Select</option>
                <option value="1.令">1.令</option>
                <option value="2.呈">2.呈</option>
                <option value="3.咨">3.咨</option>
                <option value="4.函">4.函</option>
                <option value="5.公告">5.公告</option>
                <option value="6.1書函">6.1書函</option>
                <option value="6.2開會(會勘)通知單">6.2開會(會勘)通知單</option>
                <option value="6.3簽">6.3簽</option>
                <option value="6.4移文單">6.4移文單</option>
                <option value="6.5機密文書機密等級變更或註銷建議(通知)單">6.5機密文書機密等級變更或註銷建議(通知)單</option>
            </select>
        </div>
        <!-- title field hidden initially -->
        <div class="mb-3" id="titleField">
            <label for="title" class="form-label">主旨</label>
			<textarea class="form-control" id="title" name="title" rows="2" required><?=$title;?></textarea>			
        </div>

        <!-- content field hidden initially -->
        <div class="mb-3" id="contentField">
            <label for="content" class="form-label">說明</label>
			<textarea class="form-control" id="content" name="content" rows="4" required><?=$content;?></textarea>						
        </div>

        <!-- a01 field hidden initially -->
        <div class="mb-3" id="a01Field">
            <label for="a01" class="form-label">發文單位</label>
            <input type="text" class="form-control" id="a01" name="a01" value="<?=$a01;?>">
        </div>

        <!-- a02 field hidden initially -->
        <div class="mb-3" id="a02Field">
            <label for="a02" class="form-label">受文者</label>
            <input type="text" class="form-control" id="a02" name="a02" value="<?=$a02;?>">
        </div>

        <!-- a03 field hidden initially -->
        <div class="mb-3" id="a03Field">
            <label for="a03" class="form-label">發文日期</label>
            <input type="text" class="form-control" id="a03" name="a03" value="<?=$a03;?>">
        </div>

        <!-- a04 field hidden initially -->
        <div class="mb-3" id="a04Field">
            <label for="a04" class="form-label">發文字號</label>
            <input type="text" class="form-control" id="a04" name="a04" value="<?=$a04;?>">
        </div>
		
        <!-- a05 field hidden initially -->
        <div class="mb-3" id="a05Field">
            <label for="a05" class="form-label">速別</label>
            <input type="text" class="form-control" id="a05" name="a05" value="<?=$a05;?>">
        </div>

        <!-- a06 field hidden initially -->
        <div class="mb-3" id="a06Field">
            <label for="a06" class="form-label">密等</label>
            <input type="text" class="form-control" id="a06" name="a06" value="<?=$a06;?>">
        </div>
		
        <!-- a07 field hidden initially -->
        <div class="mb-3" id="a07Field">
            <label for="a07" class="form-label">附件</label>
            <input type="text" class="form-control" id="a07" name="a07" value="<?=$a07;?>">
        </div>

        <!-- a08 field hidden initially -->
        <div class="mb-3" id="a08Field">
            <label for="a08" class="form-label">正本</label>
            <input type="text" class="form-control" id="a08" name="a08" value="<?=$a08;?>">
        </div>
		
        <!-- a09 field hidden initially -->
        <div class="mb-3" id="a09Field">
            <label for="a09" class="form-label">副本</label>
            <input type="text" class="form-control" id="a09" name="a09" value="<?=$a09;?>">
        </div>

        <!-- a10 field hidden initially -->
        <div class="mb-3" id="a10Field">
            <label for="a10" class="form-label">聯絡人</label>
            <input type="text" class="form-control" id="a10" name="a10" value="<?=$a10;?>">
        </div>
		
        <!-- a11 field hidden initially -->
        <div class="mb-3" id="a11Field">
            <label for="a11" class="form-label">地址</label>
            <input type="text" class="form-control" id="a11" name="a11" value="<?=$a11;?>">
        </div>

        <!-- a12 field hidden initially -->
        <div class="mb-3" id="a12Field">
            <label for="a12" class="form-label">電話</label>
            <input type="text" class="form-control" id="a12" name="a12" value="<?=$a12;?>">
        </div>
		
        <!-- a13 field hidden initially -->
        <div class="mb-3" id="a13Field">
            <label for="a13" class="form-label">傳真</label>
            <input type="text" class="form-control" id="a13" name="a13" value="<?=$a13;?>">
        </div>

        <!-- a14 field hidden initially -->
        <div class="mb-3" id="a14Field">
            <label for="a14" class="form-label">Email</label>
            <input type="text" class="form-control" id="a14" name="a14" value="<?=$a14;?>">
        </div>
		
        <!-- a15 field hidden initially -->
        <div class="mb-3" id="a15Field">
            <label for="a15" class="form-label">公告依據</label>
            <input type="text" class="form-control" id="a15" name="a15" value="<?=$a15;?>">
        </div>		

		<button type="submit" class="btn btn-primary btn-sm">製作公文</button><br><br>

    </form>

    <!-- Modal for showing the loading message -->
    <div class="modal fade" id="loadingModal" tabindex="-1" aria-labelledby="loadingModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="loadingModalLabel">Working...</h5>
                </div>
                <div class="modal-body">
                    請等候10秒鐘, 您的公文正在製作中.
                </div>
            </div>
        </div>
    </div>

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize input data
    $office_document = htmlspecialchars(trim($_POST['office_document']));
    $title = htmlspecialchars(trim($_POST['title']));
    $content = htmlspecialchars(trim($_POST['content']));
    // Validate input
    if (!empty($office_document) && !empty($title) && !empty($content)) {
        // 運行工作流程
        try {
            $inputs = [
                'document' => $office_document,
                'title' => $title,
                'content' => $content,
                'a01' => $a01,
                'a02' => $a02,
                'a03' => $a03,
                'a04' => $a04,
                'a05' => $a05,
                'a06' => $a06,
                'a07' => $a07,
                'a08' => $a08,
                'a09' => $a09,
                'a10' => $a10,
                'a11' => $a11,
                'a12' => $a12,
                'a13' => $a13,
                'a14' => $a14,
                'a15' => $a15,
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
?>
    <h4 class="mb-4 text-center"> [ <?=$office_document;?> ] 製作完成</h4>
    <div class="textarea-container">
    <textarea id="codeTextarea" class="textarea2 form-control mb-3">
<?php
                echo substr(trim($responseData['data']['outputs']['text']), 4, -3);
?>
    </textarea>
    </div>
    <div class="d-flex justify-content-center gap-2">
        <button class="btn btn-primary  btn-sm" onclick="copyCode()">複製公文</button>
        <button class="btn btn-secondary  btn-sm" onclick="toggleTextarea()">隱藏/開啟</button>
    </div>

    <script>
        function copyCode() {
            const textarea = document.getElementById('codeTextarea');
            textarea.select();
            textarea.setSelectionRange(0, 99999); // For mobile devices

            try {
                document.execCommand('copy');
                alert('公文已經複製到你的剪貼簿!');
            } catch (err) {
                alert('公文複製失敗');
            }
        }

        function toggleTextarea() {
            const textarea = document.getElementById('codeTextarea');
            if (textarea.style.display === 'none') {
                textarea.style.display = 'block';
            } else {
                textarea.style.display = 'none';
            }
        }
    </script>
<?php
            } else {
                echo "Error: 'outputs' or 'text' key not found in the response.";
            }
        } catch (Exception $e) {
            echo "Error: " . $e->getMessage() . PHP_EOL;
        }
    } else {
        echo "Please fill out all fields correctly.";
    }
}
?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Show the loading modal when the form is submitted
        function showLoadingModal() {
            var loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
            loadingModal.show();
        }

        // Toggle the visibility of fields based on Office Document selection
        function toggleFields() {
            const office_document = document.getElementById('office_document').value;
            const titleField = document.getElementById('titleField');
            const contentField = document.getElementById('contentField');
            const a01Field = document.getElementById('a01Field');
            const a02Field = document.getElementById('a02Field');
            const a03Field = document.getElementById('a03Field');
            const a04Field = document.getElementById('a04Field');
            const a05Field = document.getElementById('a05Field');
            const a06Field = document.getElementById('a06Field');
            const a07Field = document.getElementById('a07Field');
            const a08Field = document.getElementById('a08Field');
            const a09Field = document.getElementById('a09Field');
            const a10Field = document.getElementById('a10Field');
            const a11Field = document.getElementById('a11Field');
            const a12Field = document.getElementById('a12Field');
            const a13Field = document.getElementById('a13Field');
            const a14Field = document.getElementById('a14Field');
            const a15Field = document.getElementById('a15Field');

            // Hide both fields initially
            titleField.style.display = 'none';
            contentField.style.display = 'none';
            a01Field.style.display = 'none';
            a02Field.style.display = 'none';
            a03Field.style.display = 'none';
            a04Field.style.display = 'none';
            a05Field.style.display = 'none';
            a06Field.style.display = 'none';
            a07Field.style.display = 'none';
            a08Field.style.display = 'none';
            a09Field.style.display = 'none';
            a10Field.style.display = 'none';
            a11Field.style.display = 'none';
            a12Field.style.display = 'none';
            a13Field.style.display = 'none';
            a14Field.style.display = 'none';
            a15Field.style.display = 'none';

            // Apply logic based on the office_document selected
            if (office_document === '1.令') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '2.呈') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '3.咨') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 				
            } else if (office_document === '4.函') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 			
            } else if (office_document === '5.公告') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '6.1書函') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '6.2開會(會勘)通知單') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '6.3簽') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
                a15Field.style.display = 'block'; 
            } else if (office_document === '6.4移文單') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
            } else if (office_document === '6.5機密文書機密等級變更或註銷建議(通知)單') {
                titleField.style.display = 'block';
                contentField.style.display = 'block'; 
                a01Field.style.display = 'block'; 
                a02Field.style.display = 'block'; 
                a03Field.style.display = 'block'; 
                a04Field.style.display = 'block'; 
                a05Field.style.display = 'block'; 
                a06Field.style.display = 'block'; 
                a07Field.style.display = 'block'; 
                a08Field.style.display = 'block'; 
                a09Field.style.display = 'block'; 
                a10Field.style.display = 'block'; 
                a11Field.style.display = 'block'; 
                a12Field.style.display = 'block'; 
                a13Field.style.display = 'block'; 
                a14Field.style.display = 'block'; 
            }
        }
    </script>
</body>
</html>
