#Natural Science and Industrial Engineering Corporation

import tkinter as tk
from tkinter import filedialog, messagebox
import pypandoc
import os
import sys

class MarkdownToWordConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.md_file_path = ""
        self.template_file_path = ""
        self.output_file_path = ""
        self.ai_words_mapping = self._get_ai_words_mapping()
    
    def _get_ai_words_mapping(self):
        """返回AI高频词替换映射表"""
        return {
            # 动词类
            "优化": "改进", "提升": "提高", "构建": "建立", "部署": "布置",
            "整合": "合并", "评估": "评价", "分析": "解析", "处理": "处置",
            "执行": "实施", "完成": "完结", "使用": "采用", "利用": "运用",
            "帮助": "协助", "支持": "支撑", "促进": "推动", "增强": "加强",
            "改善": "改进", "解决": "处理", "管理": "管治", "领导": "带领",
            "指导": "指引", "建议": "提议", "计划": "规划",
            
            # 名词类
            "模型": "模式", "框架": "架构", "结构": "构造", "功能": "功用",
            "特性": "特征", "优点": "长处", "缺点": "短处", "挑战": "难题",
            "机遇": "机会", "未来": "将来", "现在": "当前", "之前": "以前",
            "之后": "以后", "同时": "一齐", "同样": "一样", "不同": "不一样",
            "各种": "多种", "每个": "每一个", "每个": "各个", "每个": "每位",
            
            # 形容词/副词类
            "重要": "关键", "非常": "十分", "很多": "许多", "一些": "有些",
            "一种": "一类", "多个": "若干", "高效": "高效果", "智能": "智慧",
            "自动": "自行", "精准": "精确", "全面": "全方位", "深入": "深刻",
            "快速": "迅速", "灵活": "灵便", "稳定": "稳固", "可靠": "可信",
            
            # 连接词/介词
            "通过": "经过", "对于": "关于", "基于": "根据", "作为": "当做",
            "因此": "所以", "然而": "但是", "此外": "另外", "例如": "比如",
            "包括": "包含", "具有": "拥有", "进行": "做", "可以": "能够",
            "应该": "应当", "需要": "必须",
            
            # 技术术语（替换为更通俗的表达）
            "算法": "计算方法", "参数": "参量", "变量": "变数", "函数": "功能",
            "接口": "交接面", "模块": "组件", "系统": "体系", "数据": "资料",
            "信息": "消息", "网络": "网路", "平台": "台子", "应用": "程式",
            "开发": "研制", "测试": "检验", "部署": "布置", "监控": "监视",
            
            # 现代流行词
            "赋能": "赋予能力", "抓手": "关键点", "闭环": "循环", "沉淀": "积累",
            "落地": "实施", "对齐": "对准", "打通": "连通", "打磨": "完善",
            "迭代": "更新", "复盘": "总结", "梳理": "整理", "输出": "产出",
            "透明": "公开", "透明化": "公开化", "维度": "角度", "场景": "情况",
            
            # 英文直译词
            "OKR": "目标与关键成果", "KPI": "关键绩效指标", "ROI": "投资回报率",
            "UI": "用户界面", "UX": "用户体验", "API": "应用程序接口",
            
            # 过度使用的抽象词
            "生态": "环境", "生态化": "环境化", "矩阵": "组合", "体系": "系统",
            "方法论": "方法", "底层逻辑": "基本原理", "顶层设计": "总体规划",
            "护城河": "竞争优势", "壁垒": "障碍", "赛道": "领域",
            
            # 夸张表达
            "革命性": "突破性", "颠覆性": "变革性", "极致": "极度", "完美": "完善",
            "绝对": "完全", "彻底": "完全", "显著": "明显", "巨大": "很大",
            
            # 商业术语
            "商业模式": "经营方式", "变现": "盈利", "流量": "访问量", "转化": "转变",
            "留存": "保持", "拉新": "吸引新用户", "促活": "促进活跃", "营收": "收入",
            
            # 教育术语
            "学习": "学", "教学": "教", "教育": "教导", "培训": "训练",
            "课程": "课", "教材": "教学材料", "评估": "评价", "反馈": "回馈"

            
        }
    
    def reduce_ai_rate(self, content):
        """降低文本的AI率，替换高频AI词汇"""
        try:
            # 对内容进行替换处理
            for ai_word, replacement in self.ai_words_mapping.items():
                content = content.replace(ai_word, replacement)
            return content
        except Exception as e:
            # 如果处理出错，返回原内容
            print(f"降AI率处理出错: {e}")
            return content

    def create_temp_markdown_file(self, original_file_path):
        """创建降AI率处理后的临时Markdown文件"""
        try:
            # 读取原始文件内容
            with open(original_file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # 进行降AI率处理
            processed_content = self.reduce_ai_rate(original_content)
            
            # 创建临时文件
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(
                mode='w', 
                suffix='.md', 
                encoding='utf-8', 
                delete=False
            )
            temp_file.write(processed_content)
            temp_file_path = temp_file.name
            temp_file.close()
            
            return temp_file_path
            
        except Exception as e:
            messagebox.showerror("文件处理错误", f"创建临时文件时出错:\n{str(e)}")
            return original_file_path  # 出错时返回原文件路径
    
    def select_markdown_file(self):
        """选择Markdown文件"""
        file_types = [
            ("Markdown文件", "*.md"),
            ("文本文件", "*.txt"),
            ("所有文件", "*.*")
        ]
        self.md_file_path = filedialog.askopenfilename(
            title="选择要转换的Markdown文件",
            filetypes=file_types
        )
        return self.md_file_path
    
    def select_template_file(self):
        """选择格式模板文件"""
        file_types = [
            ("Word文档", "*.docx"),
            ("所有文件", "*.*")
        ]
        self.template_file_path = filedialog.askopenfilename(
            title="选择格式要求文档（Word模板）",
            filetypes=file_types
        )
        return self.template_file_path
    
    def select_save_location(self):
        """选择保存位置"""
        file_types = [
            ("Word文档", "*.docx"),
            ("所有文件", "*.*")
        ]
        self.output_file_path = filedialog.asksaveasfilename(
            title="选择Word文档保存位置",
            defaultextension=".docx",
            filetypes=file_types
        )
        return self.output_file_path
    
    def get_resource_path(relative_path):
        """获取资源的绝对路径，支持打包环境和开发环境"""
        if hasattr(sys, '_MEIPASS'):
            # 打包环境
            base_path = sys._MEIPASS
        else:
            # 开发环境
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # 修改检查pandoc安装的函数
    def check_pandoc_installation(self):
        """检查pandoc是否安装"""
        try:
            # 首先尝试使用打包的pandoc（如果有）
            if hasattr(sys, '_MEIPASS'):
                pandoc_path = os.path.join(sys._MEIPASS, 'pandoc')
                if os.path.exists(pandoc_path):
                    return True
            
            # 然后检查系统安装的pandoc
            import pypandoc
            pypandoc.get_pandoc_version()
            return True
        except (ImportError, OSError) as e:
            return False
    
    def install_pandoc(self):
        """尝试安装pandoc"""
        try:
            import pypandoc
            # 下载并安装pandoc
            pypandoc.download_pandoc()
            return True
        except Exception as e:
            return False
    
    def convert_markdown_to_word(self):
        """执行Markdown到Word的转换"""
        temp_file_path = None
        try:
            # 检查必要文件是否已选择
            if not all([self.md_file_path, self.template_file_path, self.output_file_path]):
                messagebox.showerror("错误", "请确保已选择Markdown文件、模板文件和保存位置")
                return False
            
            # 检查文件是否存在
            if not os.path.exists(self.md_file_path):
                messagebox.showerror("错误", f"Markdown文件不存在: {self.md_file_path}")
                return False
            
            if not os.path.exists(self.template_file_path):
                messagebox.showerror("错误", f"模板文件不存在: {self.template_file_path}")
                return False
            
            # 询问是否进行降AI率处理
            reduce_ai = messagebox.askyesno(
                "降AI率处理", 
                "是否对文档进行降AI率处理？\n\n这将替换一些AI高频词汇，使文档更自然。"
            )
            
            # 根据选择创建临时文件或使用原文件
            if reduce_ai:
                temp_file_path = self.create_temp_markdown_file(self.md_file_path)
                input_file = temp_file_path
            else:
                input_file = self.md_file_path
            
            # 执行转换
            output = pypandoc.convert_file(
                input_file,           # 使用处理后的文件或原文件
                'docx',               # 输出格式
                outputfile=self.output_file_path,  # 输出文件
                extra_args=[
                    '--reference-doc', self.template_file_path,  # 使用模板文件
                    '--standalone',    # 生成完整文档
                    '--self-contained' # 包含所有资源
                ]
            )
            
            return True
            
        except Exception as e:
            messagebox.showerror("转换错误", f"转换过程中出现错误:\n{str(e)}")
            return False
        finally:
            # 清理临时文件
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.unlink(temp_file_path)
                except:
                    pass  # 忽略清理错误
    
    def run_conversion(self):
        """运行完整的转换流程"""
        
        # 检查pandoc是否安装[1,5](@ref)
        if not self.check_pandoc_installation():
            install_result = messagebox.askyesno(
                "缺少依赖", 
                "检测到系统未安装Pandoc，这是转换必需的组件。\n是否尝试自动安装？"
            )
            if install_result:
                if self.install_pandoc():
                    messagebox.showinfo("成功", "Pandoc安装成功！")
                else:
                    messagebox.showerror(
                        "安装失败", 
                        "Pandoc自动安装失败。\n请手动安装Pandoc：\n\n"
                        "Windows: 从 https://pandoc.org/installing.html 下载安装包\n"
                        "macOS: brew install pandoc\n"
                        "Linux: sudo apt-get install pandoc"
                    )
                    return
            else:
                return
        
        # 第一步：选择Markdown文件[6,7](@ref)
        if not self.select_markdown_file():
            messagebox.showinfo("提示", "已取消选择Markdown文件")
            return
        
        # 第二步：选择模板文件
        if not self.select_template_file():
            messagebox.showinfo("提示", "已取消选择模板文件")
            return
        
        # 第三步：选择保存位置
        if not self.select_save_location():
            messagebox.showinfo("提示", "已取消选择保存位置")
            return
        
        # 显示转换信息
        file_info = f"""
转换信息：
- Markdown文件: {os.path.basename(self.md_file_path)}
- 模板文件: {os.path.basename(self.template_file_path)}
- 输出文件: {os.path.basename(self.output_file_path)}

是否开始转换？
        """
        
        if messagebox.askyesno("确认转换", file_info):
            # 执行转换
            if self.convert_markdown_to_word():
                messagebox.showinfo("转换成功", f"Markdown文件已成功转换为Word文档！\n\n保存位置: {self.output_file_path}")
                
                # 询问是否打开生成的文档
                if messagebox.askyesno("打开文档", "是否立即打开生成的Word文档？"):
                    try:
                        os.startfile(self.output_file_path)  # Windows
                    except:
                        try:
                            # macOS 或 Linux
                            import subprocess
                            subprocess.call(['open', self.output_file_path])  # macOS
                        except:
                            try:
                                subprocess.call(['xdg-open', self.output_file_path])  # Linux
                            except:
                                messagebox.showinfo("提示", f"请手动打开文件: {self.output_file_path}")
            else:
                messagebox.showerror("转换失败", "文件转换失败，请检查错误信息。")

def main():
    """主函数"""
    converter = MarkdownToWordConverter()
    converter.run_conversion()

if __name__ == "__main__":
    main()