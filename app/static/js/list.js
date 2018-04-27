layui.use(['layer', 'flow', 'element'], function () {
    // var layer = layui.layer;
    var flow = layui.flow;
    var element = layui.element;
    // layer.open({
    //     type: 1,
    //     title: false,
    //     closeBtn: 0,
    //     shadeClose: true,
    //     content: '<div class="layui-bg-green" style="width:400px;height:400px;">aaa</div>'
    // });
    flow.load({
        elem: '#movie_list' //指定列表容器
        , isAuto: true
        , end: '~~ 我也是有底线的 ~~'
        , done: function (page, next) { //到达临界点（默认滚动触发），触发下一页
            var lis = [];
            //以jQuery的Ajax请求为例，请求下一页数据（注意：page是从2开始返回）
            $.get('/list_more/' + page, function (res) {
                //假设你的列表返回在data集合中
                layui.each(res.movies, function (index, item) {
                    html = '<div class="layui-col-xs6 layui-col-sm3 layui-col-md3" onclick="show_detail(' + item.id + ')">';
                    html += '<div class="card">';
                    html += '<div class="img_div card_img" style="background: url(' + item.cover + ') no-repeat center center;"></div>';
                    html += '<div class="card_info">';
                    html += '<span>' + item.title + '</span>';
                    html += '<div class="card_rate">';
                    html += '豆瓣评分 <span class="layui-badge">' + item.rate + '</span>';
                    html += '</div></div></div></div>';
                    lis.push(html);
                });

                //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
                //pages为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
                next(lis.join(''), page < res.total_page);
            });
        }
    });
});

function show_detail(id) {
    window.location.href = '/movie/' + id;
}