/*
 * @lc app=leetcode id=105 lang=golang
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
	var inorderMap = make([]int, 6001)
	for i := range inorder {
		inorderMap[inorder[i]+3000] = i
	}

	return helperTraverse(0, len(preorder), 0, len(inorder), preorder, inorder, inorderMap)
}

func helperTraverse(preL, preR, inL, inR int, preorder, inorder []int, inorderMap []int) *TreeNode {
	if preL == preR {
		return nil
	}

	rootVal := preorder[preL]
	inorderRootIdx := inorderMap[rootVal+3000]
	inorderLeftSize := inorderRootIdx - inL

	return &TreeNode{
		Val:   rootVal,
		Left:  helperTraverse(preL+1, preL+1+inorderLeftSize, inL, inorderRootIdx, preorder, inorder, inorderMap),
		Right: helperTraverse(preL+1+inorderLeftSize, preR, inorderRootIdx+1, inR, preorder, inorder, inorderMap),
	}
}

// @lc code=end
