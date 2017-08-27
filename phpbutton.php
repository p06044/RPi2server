<?php
  if (@$_GET['send']) {
    $fullPath = '/usr/bin/python /home/pi/weight.py';
    echo "画像ファイル更新できてます？";
    shell_exec($fullPath);
    exec('ls -lrt weight*', $out);
      print_r( $out );
  } else {
    echo "ボタン押していただけます？";
  }
?>
