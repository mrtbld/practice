TMP_DIR=/tmp/gopl/exercise1.3
mkdir -p $TMP_DIR
for f in concat join
do
    echo $f
    go build -o $TMP_DIR/echo_$f echo_$f.go
    time seq 1000 | xargs -I{} $TMP_DIR/echo_$f $(seq 1000) > /dev/null
done
rm -rf $TMP_DIR
