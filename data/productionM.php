<?php
$dbhost = 'localhost';  // mysql服务器主机地址
$dbuser = 'Chenzk';            // mysql用户名
$dbpass = 'Chenzk1';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('Could not connect: ' . mysqli_error());
}
echo '数据库连接成功！';

$sql = "CREATE TABLE IF NOT EXISTS productionM1( ".
        "month INT NOT NULL, ".
        "num INT NOT NULL,".
        "PRIMARY KEY ( month ))ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='表1,月份-产量'; ";
mysqli_select_db( $conn, 'myproject' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('数据表创建失败: ' . mysqli_error($conn));
}
echo "数据表创建成功\n";
for($i=1;$i<=12;$i++)
{
    $sql = "CREATE TABLE IF NOT EXISTS production".$i."( ".
        "id VARCHAR(100) NOT NULL COMMENT '订单号', ".
        "name VARCHAR(100) NOT NULL COMMENT '品名',".
        "num INT NOT NULL, ".
        "PRIMARY KEY ( id ))ENGINE=InnoDB DEFAULT CHARSET=utf8; ";
    mysqli_select_db( $conn, 'myproject' );
    $retval = mysqli_query( $conn, $sql );
    if(! $retval )
    {
        die('数据表创建失败: ' . mysqli_error($conn));
    }
    echo "数据表创建成功\n";
}


mysqli_close($conn);
?>